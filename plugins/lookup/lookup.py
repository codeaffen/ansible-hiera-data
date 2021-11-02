# Copyright (c) 2021 Christian Meißner
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: lookup
    author: Christian Meißner <cme+codeaffen@meissner.sh>
    version_added: "0.0.2"
    short_description: prints debug text
    description:
        - This lookup returns nothing but a text to stderr
"""
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

display = Display()


class LookupModule(LookupBase):

    def run(self, terms, **kwargs):
        self._display.display('run lookup method')

        for term in terms:
            print(type(term))

        return None
