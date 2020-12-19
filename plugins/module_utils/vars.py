# Copyright (c) 2020 Christian Meißner
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.utils.vars import merge_hash, _validate_mutable_mappings


def combine_vars(left, right, hash_behavior='merge', list_behavior='replace'):
    """Return a copy of dictionaries of variables based on configured hash behavior.

    This function takes two dictionaries and merge them according to the choosen `hash_behavior`.
    If there are elements from type `list` they were be handled according to the choosen `list_behavior`.
    All other types will replace in `left` dict by the values of `right` dict.
    The work is always done recursively.

    :param left: Dict with lower precedence.
    :type left: dict
    :param right: Dict with higher precedence.
    :type right: dict
    :param hash_behavior: How should dicts be handled, options are 'merge', 'replace', defaults to 'merge'
    :type hash_behavior: str, optional
    :param list_behavior: How should lists be handled, option are 'append', 'append_rp', 'keep', 'prepend', 'prepend_rp', 'replace', defaults to 'replace'
    :type list_behavior: str, optional
    :return: Returns a copy of `left` merged with the keys and values from `right`.
    :rtype: dict
    """
    if hash_behavior == "merge":
        return merge_hash(left, right, recursive=True, list_merge=list_behavior)
    else:
        # HASH_BEHAVIOUR == 'replace'
        _validate_mutable_mappings(left, right)
        result = left.copy()
        result.update(right)
        return result
