=================================
codeaffen.hieradata Release Notes
=================================

.. contents:: Topics


v0.1.0
======

Minor Changes
-------------

- Add a wrapper function `combine_vars` to be compatible to default ansible.
- Add configuration parameters to manage hash and list behavior.
- Add method to parse configuration file (e.g. hieradata.yml).
- After loading, the vars will be combined with ansible functions.
- Change parameter names. Remove prefix to make documentation more clear.
- If last part is directory it can have no, one or multiple files in it.
- Last part of hierarchy can be file or directory.
- Load files from hierarchy.
- Parse entity name into hiera_vars dict.
- The hiera_vars dict can be used to generate a dynamic hierarchy.
- These function tages two extra parameters `hash_behavior` and `list_behavior` to configure this feature as needed.

v0.0.1
======

New Plugins
-----------

Vars
~~~~

- codeaffen.hieradata.hieradata - Loads configuration from a hierarchical configuration structure structure
