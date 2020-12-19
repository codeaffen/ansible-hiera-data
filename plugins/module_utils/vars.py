# Copyright (c) 2020 Christian Meißner
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.utils.vars import merge_hash, _validate_mutable_mappings


def combine_vars(a, b, hash_behavior='merge', list_behavior='replace'):
    """
    Return a copy of dictionaries of variables based on configured hash behavior
    """

    if hash_behavior == "merge":
        return merge_hash(a, b, recursive=True, list_merge=list_behavior)
    else:
        # HASH_BEHAVIOUR == 'replace'
        _validate_mutable_mappings(a, b)
        result = a.copy()
        result.update(b)
        return result
