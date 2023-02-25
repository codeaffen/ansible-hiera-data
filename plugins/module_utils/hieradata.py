# Copyright (c) 2020 Christian Meißner
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import yaml

from jinja2 import Template
from yaml.loader import SafeLoader


def parse_config(entity, config):
    """Load hieradata.yml and parse its content.

    :param entity: the entity for what the configuration will be parsed
    :type entity: str
    :param parse: the type of entity we want to parse the configuration, defaults to "both"
    :type parse: str, optional
    :return: list of paths which reflects the hierarchy
    :rtype: list
    """
    hierarchy = None
    if os.path.exists(config) and os.path.isfile(config):
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
