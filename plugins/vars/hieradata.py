# Copyright (c) 2020 Christian Meißner
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: hieradata
    version_added: "0.0.1"
    short_description: Loads configuration from a hierarchical configuration structure
    requirements:
        - whitelist in configuration
    description:
        - Loads YAML vars into corresponding hierarchy directories/files.
        - Loads only files with extension to one of .yaml, .json, .yml or no extension.
        - Starting in 0.0.1, this plugin requires explicit whitelisting via I(vars_plugins_enabled).
    options:
      hiera_basedir:
        default: "hieradata"
        description:
            - The base directory where the hierarchy has to be placed in.
            - The base directory has to be placed within the inventory directory or playbook directory.
        type: str
        env:
          - name: HIERADATA_BASE_DIR
        ini:
          - section: hieradata
            key: basedir
      hiera_config:
        default: hieradata.yml
        description:
          - Name of hieradata configuration file.
          - The hieradata configuration file has to be placed within the inventory dirctory or playbook directory.
        type: str
        env:
          - name: HIERADATA_CONFIG_FILE
        ini:
          - section: hieradata
            key: config
      stage:
        ini:
          - section: hieradata
            key: stage
        env:
          - name: HIERADATA_VARS_PLUGIN_STAGE
      _valid_extensions:
        default: [".yml", ".yaml", ".json"]
        description:
          - "Check all of these extensions when looking for 'variable' files which should be YAML or JSON or vaulted versions of these."
          - 'This affects vars_files, include_vars, inventory and vars plugins among others.'
        env:
          - name: ANSIBLE_YAML_FILENAME_EXT
        ini:
          - section: yaml_valid_extensions
            key: defaults
        type: list
    extends_documentation_fragment:
      - vars_plugin_staging
'''

EXAMPLES = '''
# hieradata.yml.
# Each level in hierarchy can be a file or a directory.
hiera_vars:
  role: "{{ entity.name.split('-').0 }}"
  env: "{{ entity.name.split('-').2 }}"
hierarchy:
  - common
  - "{{ env }}"
  - "{{ role }}"
  - "{{ role }}-{{ env }}"

# hieradata organized with sub directories.
# Last part of path of each level can be a file or a directory.
hiera_vars:
  role: "{{ entity.name.split('-').0 }}"
  env: "{{ entity.name.split('-').2 }}"
hieradata:
  hierarchy:
    - common
    - "environments/{{ env }}"
    - "roles/{{ role }}"
    - "roles/{{ role }}-{{ env }}"
'''

import inflection
import os
import yaml

from jinja2 import Template
from yaml.loader import SafeLoader

from ansible import constants as C
from ansible.errors import AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.plugins.vars import BaseVarsPlugin
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.utils.vars import combine_vars

FOUND = {}


class VarsModule(BaseVarsPlugin):

    def get_vars(self, loader, path, entities, cache=True):
        """parse the inventory file.

        :param loader: The DataLoader wich auto-load JSON/YAML and decrypt vaulted data, and cache read files.
        :type loader: DataLoader
        :param path: Directory data for inventory and current playbook directory, to find data in reference to them.
        :type path: list
        :param entities: Host and group names for what variables are needed. The plugin is called once for hosts and for groups too.
        :type entities: list
        :param cache: If true use cached values to reduce costs of re-reading., defaults to True
        :type cache: boolean, optional
        :return: Dictionary structure with the variables loaded from files.
        :rtype: dictionary
        """
        if not isinstance(entities, list):
            entities = [entities]

        super(VarsModule, self).get_vars(loader, path, entities)

        self.hiera_basedir = self.get_option('hiera_basedir')
        self.hiera_config = self.get_option('hiera_config')

        hieradata = {}
        for entity in entities:
            hierarchy = self._parse_config(entity, os.path.join(self._basedir, self.hiera_config))
            if isinstance(entity, Host):
                if not entity.name.startswith(os.path.sep) and hierarchy is not None:
                    found_files = []
                    for level in hierarchy:
                        l_dirname = os.path.join(self.hiera_basedir, os.path.dirname(level))
                        l_basename = os.path.basename(level)
                        b_path = os.path.realpath(to_bytes(os.path.join(self._basedir, l_dirname)))
                        t_path = to_text(b_path)
                        try:
                            # load vars
                            if cache and level in FOUND:
                                found_files = FOUND[level]
                            else:
                                # if basedir for that level doesn't exists, we don't have to do anything here
                                if os.path.exists(b_path):
                                    if os.path.isdir(b_path):
                                        self._display.debug("\tprocessing dir {0}".format(t_path))
                                        found_files = loader.find_vars_files(t_path, l_basename)
                                        FOUND[level] = found_files
                                    else:
                                        self._display.warning("Found {0} that is not a directory, skipping: {1}".format(l_dirname, t_path))

                            for found in found_files:
                                new_data = loader.load_from_file(found, cache=True, unsafe=True)
                                if new_data:  # ignore empty files
                                    hieradata = combine_vars(hieradata, new_data)

                        except Exception as e:
                            raise AnsibleParserError(to_native(e))

        return hieradata

    def _parse_config(self, entity, config):
        """Loads hieradata.yml and parse its content

        :param entity: the entity for what the configuration will be parsed
        :type entity: str
        :param parse: the type of entity we want to parse the configuration, defaults to "both"
        :type parse: str, optional
        :return: list of paths which reflects the hierarchy
        :rtype: list
        """
        with open(config) as fd:
            fd_data = yaml.load(fd, Loader=SafeLoader)

        hiera_vars = {}
        for k, v in fd_data['hiera_vars'].items():
            t = Template(v)
            hiera_vars[k] = t.render(entity=entity)

        hierarchy = []
        for i, entry in enumerate(fd_data['hierarchy']):
            t = Template(entry)
            hierarchy.insert(i, t.render(hiera_vars))

        return hierarchy
