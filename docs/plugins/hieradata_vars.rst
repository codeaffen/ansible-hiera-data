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

- Loads YAML vars into corresponding hierarchy directories/files.
- Loads only files with extension to one of .yaml, .json, .yml or no extension.
- Starting in 0.0.1, this plugin requires explicit whitelisting via *vars_plugins_enabled*.


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
                                env:HIERADATA_BASE_DIR
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>The base directory where the hierarchy has to be placed in.</div>
                                            <div>The base directory has to be placed within the inventory directory or playbook directory.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"hieradata.yml"</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [hieradata]<br>config = hieradata.yml
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:HIERADATA_CONFIG_FILE
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Name of hieradata configuration file.</div>
                                            <div>The hieradata configuration file has to be placed within the inventory dirctory or playbook directory.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hash_behavior"></div>
                    <b>hash_behavior</b>
                    <a class="ansibleOptionLink" href="#parameter-hash_behavior" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>merge</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>replace</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [hieradata]<br>hash_behavior = merge
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:HIERADATA_HASH_BEHAVIOR
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>This setting defines how hashes will be merged.</div>
                                            <div>By default hieradata will merge hashes, so data only exists in higher precedence will be added to the data with lower precedence.</div>
                                            <div>Higher precedence value will override lower precedence values.</div>
                                            <div>You can define replace if you want to override data with lower precedence.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-list_behavior"></div>
                    <b>list_behavior</b>
                    <a class="ansibleOptionLink" href="#parameter-list_behavior" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>append</li>
                                                                                                                                                                                                <li>append_rp</li>
                                                                                                                                                                                                <li>keep</li>
                                                                                                                                                                                                <li>prepend</li>
                                                                                                                                                                                                <li>prepend_rp</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>replace</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [hieradata]<br>list_behavior = replace
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:HIERADATA_HASH_BEHAVIOR
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>This setting defines how lists will be handled.</div>
                                            <div>By default data with higher precedence will `replace` data with lower precedence.</div>
                                            <div>You can also append or prepend data with higher precedence.</div>
                                            <div>With replace you can override data with lower precedece by data with higher one.</div>
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
                                        [hieradata]<br>stage = None
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:HIERADATA_VARS_PLUGIN_STAGE
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

Examples
--------

.. code-block:: yaml+jinja

    
    # hieradata.yml.
    # Each level in hierarchy can be a file or a directory.
    hiera_vars:
      role: "{{ entity.name.split('-').0 }}"
      env: "{{ entity.name.split('-').2 }}"
    hierarchy:
      - common
      - "{{ env }}"
      - "{{ role }}"
      - "{{ role }}-{{ env }}"

    # hieradata organized with sub directories.
    # Last part of path of each level can be a file or a directory.
    hiera_vars:
      role: "{{ entity.name.split('-').0 }}"
      env: "{{ entity.name.split('-').2 }}"
    hieradata:
      hierarchy:
        - common
        - "environments/{{ env }}"
        - "roles/{{ role }}"
        - "roles/{{ role }}-{{ env }}"




.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors



.. Parsing errors

