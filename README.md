# Ansible Hieradata

This collection provides plugins to manage your project configuration data in a hierarchical manner like [puppet](https://puppet.com/docs/puppet/6.17/hiera_quick.html) do.

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

## Configuraton

### vars plugin configuration

The plugin comes with useful defaults to start to use the `hieradata` vars plugin without any configuration.

But if you need to customize the configuration you can see in
[documentation](https://ansible-hiera-data.readthedocs.io/en/latest/plugins/hieradata_vars.html#ansible-collections-codeaffen-hieradata-hieradata-vars)
you can configure the vars plugin eigther via `ansible.cfg` parameter in section `hieradata` or via environment variables.

You have to keep in mind that the paths for `basedir` and `config` are relative to your inventory directory. Without any configuration you have to place
the basedir and config as followed.

```bash
.
├── ansible.cfg
├── hieradata
├── hieradata.yml
└── hosts
```

If you want to use a different base then `hieradata` you can override it by exporting `HIERADATA_BASE_DIR` environment variable. This directory also has to belongs to inventory dirctory.

```bash
.
├── ansible.cfg
└── inventory
    ├── hieradata
    │   └── customer_a
    ├── hieradata.yml
    └── hosts
```

In this example you need to do `export HIERADATA_BASE_DIR=hieradata/customer_a` if you want to use `hieradata/customer_a` as hiera basedir.

## Documentation

### readthedocs.io

Current documentation can be found on [readthedocs.io](https://ansible-hiera-data.readthedocs.io/en/devel).

### repository folder

A last option to read the docs is the docs folder in this repository.

## Dependencies

The following dependencies have to be fulfiled by the Ansible controller.

* ...
