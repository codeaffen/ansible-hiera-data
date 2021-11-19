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
      basedir:
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
      config:
        default: hieradata.yml
        description:
          - Name of hieradata configuration file.
          - The hieradata configuration file has to be placed within the inventory directory or playbook directory.
          - If you want to use a different file location, you can add a path relative to the inventory or playbook directory to the file.
        type: str
        env:
          - name: HIERADATA_CONFIG_FILE
        ini:
          - section: hieradata
            key: config
      hash_behavior:
        default: merge
        description:
          - This setting defines how hashes will be merged.
          - By default hieradata will merge hashes, so data only exists in higher precedence will be added to the data with lower precedence.
          - Higher precedence value will override lower precedence values.
          - You can define replace if you want to override data with lower precedence.
        choices: ['merge', 'replace']
        type: str
        env:
          - name: HIERADATA_HASH_BEHAVIOR
        ini:
          - section: hieradata
            key: hash_behavior
      list_behavior:
        default: replace
        description:
          - This setting defines how lists will be handled.
          - By default data with higher precedence will `replace` data with lower precedence.
          - You can also append or prepend data with higher precedence.
          - With replace you can override data with lower precedece by data with higher one.
        choices: ['append', 'append_rp', 'keep', 'prepend', 'prepend_rp', 'replace']
        type: str
        env:
          - name: HIERADATA_HASH_BEHAVIOR
        ini:
          - section: hieradata
            key: list_behavior
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

import os

from ansible.errors import AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.plugins.vars import BaseVarsPlugin
from ansible.inventory.host import Host
from ansible_collections.codeaffen.hieradata.plugins.module_utils.vars import combine_vars
from ansible_collections.codeaffen.hieradata.plugins.module_utils.hieradata import parse_config
from ansible.utils.display import Display

FOUND = {}
display = Display()


class VarsModule(BaseVarsPlugin):

    def get_vars(self, loader, path, entities, cache=True):  # noqa: C901
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

        self.hiera_basedir = self.get_option('basedir')
        self.hiera_config = self.get_option('config')
        self.hiera_hash_behavior = self.get_option('hash_behavior')
        self.hiera_list_behavior = self.get_option('list_behavior')

        hieradata = {}
        for entity in entities:
            if isinstance(entity, Host):
                hierarchy = parse_config(entity, os.path.join(self._basedir, self.hiera_config))
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
                                    hieradata = combine_vars(hieradata, new_data, self.hiera_hash_behavior, self.hiera_list_behavior)

                        except Exception as e:
                            raise AnsibleParserError(to_native(e))

        return hieradata
