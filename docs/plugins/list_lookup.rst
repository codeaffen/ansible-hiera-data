.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na

.. Anchors

.. _ansible_collections.codeaffen.hieradata.list_lookup:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

codeaffen.hieradata.list -- simply returns what it is given.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `codeaffen.hieradata collection <https://galaxy.ansible.com/codeaffen/hieradata>`_ (version 0.1.0).

    To install it use: :code:`ansible-galaxy collection install codeaffen.hieradata`.

    To use it in a playbook, specify: :code:`codeaffen.hieradata.list`.

.. version_added

.. versionadded:: 2.0 of codeaffen.hieradata

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- this is mostly a noop, to be used as a with_list loop when you dont want the content transformed in any way.


.. Aliases


.. Requirements


.. Options


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: unlike with_items you will get 3 items from this loop, the 2nd one being a list
      debug: var=item
      with_list:
        - 1
        - [2,3]
        - 4




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this lookup:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-_list"></div>
                    <b>_list</b>
                    <a class="ansibleOptionLink" href="#return-_list" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=any</span>                    </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>basically the same as you fed in</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Ansible Core Team



.. Parsing errors

