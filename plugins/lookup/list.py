# Copyright (c) 2021 Christian Meißner
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: list
    author: Christian Meißner <cme+codeaffen@meissner.sh>
    version_added: "0.0.2"
    short_description: simply returns what it is given.
    description:
      - this is mostly a noop, to be used as a with_list loop when you dont want the content transformed in any way.
"""

EXAMPLES = """
- name: unlike with_items you will get 3 items from this loop, the 2nd one being a list
  debug: var=item
  with_list:
    - 1
    - [2,3]
    - 4
"""

RETURN = """
  _list:
    description: basically the same as you fed in
    type: list
    elements: raw
"""

from ansible.module_utils.common._collections_compat import Sequence
from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def run(self, terms, **kwargs):
        if not isinstance(terms, Sequence):
            raise AnsibleError("with_list expects a list")
        return terms
