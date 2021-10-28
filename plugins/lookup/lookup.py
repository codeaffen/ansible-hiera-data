# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
        lookup: lookup
        author: Christian Meißner <cme+codeaffen@meissner.sh>
        version_added: "0.0.2"
        short_description: prints debug text
        description:
            - This lookup returns nothing but a text to stderr
        # options:
        #   _terms:
        #     description: path(s) of files to read
        #     required: True
        # notes:
        #   - if read in variable context, the file can be interpreted as YAML if the content is valid to the parser.
        #   - this lookup does not understand globing --- use the fileglob lookup instead.
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
