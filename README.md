# Ansible Hieradata

This collection provides plugins to manage your project configuration data in a hierarchical manner like [puppet](https://puppet.com/docs/puppet/6.17/hiera_quick.html) do.

You will be able to use different backends for secrets like `keepass` and others.

## Installation

The collection is available via [Ansible Galaxy](https://galaxy.ansible.com/codeaffen/hieradata). So you can run

```bash
ansible-galaxy collection install codeaffen.hieradata
```

Alternatively you can build and install the collection from source.

```bash
make dist
ansible-galaxy collection install codeaffen-hieradata-<version>.tar.gz
```

## Documentation

### readthedocs.io

Current documentation can be found on [readthedocs.io](https://ansible-hiera-data.readthedocs.io/en/devel).

### repository folder

A last option to read the docs is the docs folder in this repository.

## Dependencies

The following dependencies have to be fulfiled by the Ansible controller.

* ...
