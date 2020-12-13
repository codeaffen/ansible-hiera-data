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
        - Loads YAML vars into corresponding groups/hosts in group_vars/ and host_vars/ directories.
        - Loads only files with extension to one of .yaml, .json, .yml or no extension.
        - Starting in 0.0.1, this plugin requires whitelisting and is whitelisted by default.
    options:
      hiera_basedir:
        default: "hieradata"
        description: The base directory where the hierarchy has to be placed in.
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
        type: str
        env:
          - name: HIERADATA_CONFIG_FILE
        ini:
          - section: hieradata
            key: config
      hiera_data_for:
        default: both
        choices: [hosts, groups, both]
        description:
          - Should be data loaded for I(hosts), I(groups) or I(both).
          - I case of I(both) the I(basedir) exists in sub direcoties I(host_vars) and I(group_vars) and there the defined hierarchy.
          - If you choose I(hosts) or I(groups) the I(basedir) exists in inventory directory or playbook directory and there the defined hierarchy.
        ini:
          - section: hieradata
            key: load_data_for
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
# hieradata.yml organized with files
hierarchy:
  - common.yml
  - "{{ env }}.yml"
  - "{{ role }}.yml"
  - "{{ role }}-{{ env }}.yml"

# hieradata.yml organized with directories and files
hieradata:
  hierarchy:
    - common.yml
    - "environments/{{ env }}.yml"
    - "roles/{{ role }}.yml"
    - "roles/{{ role }}-{{ env }}.yml"
'''

import inflection
import os
import yaml

from jinja2 import Template
from yaml.loader import SafeLoader

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
        self.hiera_data_for = self.get_option('hiera_data_for')
        self.hiera_config = self.get_option('hiera_config')

        hieradata = {}
        for entity in entities:
            hierarchy = self._parse_config(entity, parse=self.hiera_data_for)

            if self.hiera_data_for == 'hosts' or self.hiera_data_for == 'groups':
                hiera_basedir = os.path.join(self.hiera_basedir)
            elif isinstance(entity, Host) and self.hiera_data_for == 'both':
                hiera_basedir = os.path.join(self.hiera_basedir, 'host_vars')
            elif isinstance(entity, Group) and self.hiera_data_for == 'both':
                hiera_basedir = os.path.join(self.hiera_basedir, 'group_vars')
            else:
                raise AnsibleParserError("Supplied entity must be Host or Group, got %s instead" % (type(entity)))

        for i, entry in enumerate(hierarchy):
            t = Template(entry)
            # currently statically
            # TODO: handover variables to `get_vars`
            hierarchy[i] = t.render(role='web', env='test')

        self._display.display(u"hierarchy: {}".format(hierarchy))

        hieradata = {}

        return hieradata

    def _parse_config(self, entity, parse="both"):
        """Loads hieradata.yml and parse its content

        :param entity: the entity for what the configuration will be parsed
        :type entity: str
        :param parse: the type of entity we want to parse the configuration, defaults to "both"
        :type parse: str, optional
        :return: list of paths which reflects the hierarchy
        :rtype: list
        """
        if inflection.singularize(parse) == type(entity).__name__.lower() or parse == "both":
            with open(self.hiera_config) as fd:
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
        else:
            return None
