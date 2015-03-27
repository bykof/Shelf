import ConfigParser
import os

from fabric.api import local, settings, env
from fabric.colors import green


def setup_local():
    local_virtualenv = 'virtualenv/bin/'
    local_secrets = 'secrets.cfg'
    virtualenv_python = local_virtualenv + 'python'
    virtualenv_pip = local_virtualenv + 'pip'

    with settings(warn_only=True):
        local('rm -rf virtualenv')

    # Install virtualenv
    local('virtualenv virtualenv')
    local(virtualenv_pip + ' install -r requirements/local.txt')

    # Install Configs
    if not os.path.isfile(local_secrets):
        config_file = open('secrets.cfg', 'w+')
        config = ConfigParser.ConfigParser()

        # Database
        config.add_section('database')
        config.set('database', 'db_name', 'REPLACE_ME')
        config.set('database', 'username', 'REPLACE_ME')
        config.set('database', 'password', 'REPLACE_ME')
        config.set('database', 'host', 'REPLACE_ME')

        # LDAP Sync
        config.add_section('ldap-sync')
        config.set('ldap-sync', 'server_uri', 'REPLACE_ME')
        config.set('ldap-sync', 'sync_base', 'REPLACE_ME')
        config.set('ldap-sync', 'base_user', 'REPLACE_ME')
        config.set('ldap-sync', 'password', 'REPLACE_ME')

        # LDAP Login
        config.add_section('ldap-login')
        config.set('ldap-login', 'server_uri', 'REPLACE_ME')
        config.set('ldap-login', 'bind_dn', 'REPLACE_ME')
        config.set('ldap-login', 'password', 'REPLACE_ME')
        config.set('ldap-login', 'user_search', 'REPLACE_ME')
        config.set('ldap-login', 'group_search', 'REPLACE_ME')
        config.set('ldap-login', 'user_flags_by_group__is_active', 'REPLACE_ME')
        config.set('ldap-login', 'user_flags_by_group__is_staff', 'REPLACE_ME')
        config.set('ldap-login', 'user_flags_by_group__is_superuser', 'REPLACE_ME')
        config.write(config_file)
        config_file.close()

    # Migrate
    local(virtualenv_python + ' src/manage.py migrate')
    print(green('Your local development is ready to use! Have fun :*'))
