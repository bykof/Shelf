from fabric.api import local, settings, env
from fabric.colors import green


def setup_local():
    local_virtualenv = 'virtualenv/bin/'
    virtualenv_python = local_virtualenv + 'python'
    virtualenv_pip = local_virtualenv + 'pip'

    with settings(warn_only=True):
        local('rm -rf virtualenv')

    local('virtualenv virtualenv')
    local(virtualenv_pip + ' install -r requirements/local.txt')
    local(virtualenv_python + ' src/manage.py migrate')
    print(green('Your local development is ready to use! Have fun :*'))
