.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.codeaffen.hieradata.hieradata_vars:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

codeaffen.hieradata.hieradata -- Loads configuration from a hierarchical configuration structure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `codeaffen.hieradata collection <https://galaxy.ansible.com/codeaffen/hieradata>`_.

    To install it use: :code:`ansible-galaxy collection install codeaffen.hieradata`.

    To use it in a playbook, specify: :code:`codeaffen.hieradata.hieradata`.

.. version_added

.. versionadded:: 0.0.1 of codeaffen.hieradata

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Loads YAML vars into corresponding groups/hosts in group_vars/ and host_vars/ directories.
- Loads only files with extension to one of .yaml, .json, .yml or no extension.
- Starting in 0.0.1, this plugin requires whitelisting and is whitelisted by default.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the local controller node that executes this vars.

- whitelist in configuration


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                            <th>Configuration</th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-_valid_extensions"></div>
                    <b>_valid_extensions</b>
                    <a class="ansibleOptionLink" href="#parameter-_valid_extensions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[".yml", ".yaml", ".json"]</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [yaml_valid_extensions]<br>defaults = ['.yml', '.yaml', '.json']
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_YAML_FILENAME_EXT
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Check all of these extensions when looking for &#x27;variable&#x27; files which should be YAML or JSON or vaulted versions of these.</div>
                                            <div>This affects vars_files, include_vars, inventory and vars plugins among others.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-basedir"></div>
                    <b>basedir</b>
                    <a class="ansibleOptionLink" href="#parameter-basedir" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"hieradata"</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [hieradata]<br>basedir = hieradata
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_HIERA_DATA_DIR
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Base directory for hierdata</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hierachy"></div>
                    <b>hierachy</b>
                    <a class="ansibleOptionLink" href="#parameter-hierachy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [hieradata]<br>hierarchy = None
                                                                                                                    </p>
                                                            </div>
                                                                                            </td>
                                                <td>
                                            <div>List of files and directories that build the hierarchy</div>
                                            <div>Fist element has lowest precedence</div>
                                            <div>Last element has highest precedence</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-stage"></div>
                    <b>stage</b>
                    <a class="ansibleOptionLink" href="#parameter-stage" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 2.10 of ansible.builtin
                      </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>all</li>
                                                                                                                                                                                                <li>task</li>
                                                                                                                                                                                                <li>inventory</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [vars_host_group_vars]<br>stage = None
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_VARS_PLUGIN_STAGE
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Control when this vars plugin may be executed.</div>
                                            <div>Setting this option to <code>all</code> will run the vars plugin after importing inventory and whenever it is demanded by a task.</div>
                                            <div>Setting this option to <code>task</code> will only run the vars plugin whenever it is demanded by a task.</div>
                                            <div>Setting this option to <code>inventory</code> will only run the vars plugin after parsing inventory.</div>
                                            <div>If this option is omitted, the global <em>RUN_VARS_PLUGINS</em> configuration is used to determine when to execute the vars plugin.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso


.. Examples



.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors



.. Parsing errors

