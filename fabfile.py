# -*- coding: utf-8 -*-
"""
Allow to automate the deployment of your Django app according to a chosen environment (dev, staging, production).

    1 - Set the environment and the corresponding parameters
    2 - Deploy:
          optional: user, base_dir, project_name
          ie: fab dev deploy
              fab dev:user=[USERNAME],base_dir=[BASEDIR],project_name=[PROJECTNAME] deploy
          Actions during deploy:
            - make_settings()
            - create_virtualenv()
            - install_requirements()
            - migrate()
            - create_super_user()
            - collectstatic()

    3 - Update:
          optional: user, base_dir, project_name
          ie: fab dev update
              fab dev:user=[USERNAME],base_dir=[BASEDIR],project_name=[PROJECTNAME] deploy
          Actions during deploy:
            - install_requirements()
            - migrate()
            - collectstatic()

Requirements:
    virtualenv (https://virtualenv.pypa.io)
    virtualenvwrapper (https://virtualenvwrapper.readthedocs.io/)
    fabric (http://www.fabfile.org/)

Note:
    The production / staging environments are configured for alwaysdata server (http://www.alwaysdata.com)
    If you want to use something else, you need to change env.hosts
"""

#TODO: add try/except; test

import os
from contextlib import contextmanager as _contextmanager
from fabric.api import cd, env, run, prefix
from fabric.operations import prompt
from fabric.colors import green, blue, red


#######################
# Set parameters      #
#######################
def get_base_dir(base_dir=None):
    """
    Root path of the project.

    By default the os.path.dirname is used
    You can set it up
    1/ via the terminal prompt
    or
    2/ as a parameter when you launch this fabfile (ie: fab dev deploy:base_dir=[BASEDIR])

    :return env.base_dir
    """
    env.base_dir = base_dir
    default_base_dir = os.path.dirname(os.path.abspath(__file__))
    if not env.base_dir:
        env.base_dir = prompt('Please specify the project path root: ', default=default_base_dir)

def get_project_name(project_name=None):
    """
    Set the project name
    You can set it up
    1/ via the terminal prompt
    or
    2/ as a parameter when you launch this fabfile (ie: fab dev deploy:project_name=[PROJECTNAME])

    :return env.project_name
    """
    env.project_name = project_name
    if not env.project_name:
        env.project_name = prompt('Please specify project name: ')

def get_username(user=None):
    """
    Set the username
    You can set it up
    1/ via the terminal prompt
    or
    2/ as a parameter when you launch this fabfile (ie: fab dev deploy:user=[USER])

    :return env.user
    """
    env.user = user
    if not env.user:
        env.user = prompt('Please specify username: ')

def test_prompt(user=None):
    get_username(user)
    print env.user

#######################
# Prepare environment #
#######################
def development(user=None, base_dir=None, project_name=None):
    """
    Set environment variables for dev
    """
    print blue('BASIC INFORMATIONS:')
    get_project_name(project_name)
    get_base_dir(base_dir)
    env.hosts = ['127.0.0.1']
    env.environment = "dev"

def staging(user=None, base_dir=None, project_name=None):
    """
    Set environment variables for staging
    """
    print blue('BASIC INFORMATIONS:')
    get_project_name(project_name)
    get_username(user)
    get_base_dir(base_dir)
    env.hosts = ['%(user)s@ssh-%(user)s.alwaysdata.net' % (env, env)]
    env.environment = "staging"

def production(user=None, base_dir=None, project_name=None):
    """
    Set environment variables for production
    """
    print blue('BASIC INFORMATIONS:')
    get_project_name(project_name)
    get_username(user)
    get_base_dir(base_dir)
    env.hosts = ['%(user)s@ssh-%(user)s.alwaysdata.net' % (env, env)]
    env.environment = "prod"

######################
# Commands Shortcuts #
######################
def dev(user=None, base_dir=None, project_name=None):
    """ Shortcut for development"""
    development(user, base_dir, project_name)

def prod(user=None, base_dir=None, project_name=None):
    """ Shortcut for production"""
    production(user, base_dir, project_name)

def deploy():
    """ Group all actions to deploy the project """
    git_pull()
    if not env.environment == "dev":
        make_settings()
    else:
        make_settings_dev()
    create_virtualenv()
    install_requirements()
    migrate()
    create_super_user()
    collectstatic()
    print(green("DEPLOYMENT SUCCESSFULLY COMPLETED !!"))

def update():
    """ Group all actions to update the project """
    git_pull()
    install_requirements()
    migrate()
    collectstatic()
    print(green("SUCCESSFUL UPDATE !!"))


####################
# Commands details #
####################

def make_project_structure():
    """ Create a standard django project or django-cms project"""
    env.project_type = prompt(
        'Please specify the project type (default [0]) \n[0] django standard \n[1] django cms \n',
        default='0',
        validate='^[0,1]$'
    )

    base_dir = env.base_dir

    if env.project_type == 0:
        # standard project
        run("cp -r %s/core/project_sample/standard/apps.py %s/core/settings/apps.py" % (base_dir, base_dir))
        run("cp -r %s/core/project_sample/standard/base.py %s/core/settings/base.py" % (base_dir, base_dir))
        run("cp -r %s/core/project_sample/standard/urls.py %s/core/urls.py" % (base_dir, base_dir))
        run("rm -r %s/core/project_sample/")

    else:
        # cms project
        run("cp -r %s/core/project_sample/cms/apps.py %s/core/settings/apps.py" % (base_dir, base_dir))
        run("cp -r %s/core/project_sample/cms/base.py %s/core/settings/base.py" % (base_dir, base_dir))
        run("cp -r %s/core/project_sample/cms/urls.py %s/core/cms_toolbars.py" % (base_dir, base_dir))
        run("cp -r %s/core/project_sample/cms/urls.py %s/core/urls.py" % (base_dir, base_dir))
        run("rm -r %s/core/project_sample/")

    print green('- Generate structure Ok')



def git_pull():
    """ pull the git deposit """
    with cd(env.base_dir):
        run('git pull origin master')
    print green('- Git pull Ok !')


def make_settings_dev():
    """
    Creating the settings file for the desired environment
    Copy the sample settings, rename it according to the environment, set up the necessary variables (with prompt)
    """
    base_dir = env.base_dir
    run("cp -r %s/core/settings/local_sample_dev.py %s/core/settings/local.py" % (base_dir, base_dir))

    print green('- Generate staging Settings file Ok')

def make_settings():
    """
    Creating the settings file for the desired environment
    Copy the sample settings, rename it according to the environment, set up the necessary variables (with prompt)
    """
    base_dir = env.base_dir
    run("cp -r %s/core/settings/local_sample.py %s/core/settings/local.py" % (base_dir, base_dir))

    # Read in the file
    with cd(env.base_dir):
        file_path = '%s/core/settings/local_%s.py' % (base_dir, env.environment)
        with open(file_path, 'r') as file :
          filedata = file.read()

        # Replace the target string
        print blue('SETTING INFORMATION (env: %s):' % env.environment)

        filedata = filedata.replace('{ALLOWED_HOSTS}', prompt('ALLOWED_HOSTS (format: \'site1.com\', \'site2.com\'): '))
        filedata = filedata.replace('{SITE_URL}', '\'%s\'' % prompt('SITE_URL: '))
        filedata = filedata.replace('{EMAIL_HOST}', '\'%s\'' % prompt('EMAIL_HOST: ', default='smtp-%s.alwaysdata.net' % env.user))
        filedata = filedata.replace('{DEFAULT_FROM_EMAIL}',  '\'%s\'' % prompt('DEFAULT_FROM_EMAIL: '))
        filedata = filedata.replace('{ADMIN_EMAIL}', '\'%s\'' % prompt('ADMIN_EMAIL: '))
        filedata = filedata.replace('{CLIENT_EMAIL}', '\'%s\'' % prompt('CLIENT_EMAIL: '))
        filedata = filedata.replace('{DB_HOST}', '\'%s\'' % prompt('DB_HOST: ', default='postgresql-%s.alwaysdata.net' % env.user))
        filedata = filedata.replace('{DB_NAME}', '\'%s\'' % prompt('DB_NAME: '))
        filedata = filedata.replace('{DB_USER}', '\'%s\'' % prompt('DB_USER: '))
        filedata = filedata.replace('{DB_PASSWORD}', '\'%s\'' % prompt('DB_PASSWORD: '))

        # Write the file out again
        with open(file_path, 'w') as file:
          file.write(filedata)

        print green('- Generate Settings file Ok')

def create_virtualenv():
    """ Create a new virtualenv """
    with prefix('WORKON_HOME=~/.virtualenvs'):
        with prefix('source ~/.local/bin/virtualenvwrapper.sh'):
            run("mkvirtualenv %s" % env.project_name)
    print green('- Create virtualenv Ok')

def install_requirements():
    """ Pip install of the requirements """
    with virtualenv():
        run("pip install -r requirements.txt")
    print green('- Install Requirements Ok')

def migrate():
    """ Migrate the db """
    """ Run South migrations """
    with virtualenv():
        run("python manage.py migrate")
    print green('- Migration Ok')

def collectstatic():
    """ Collect static files from installed apps """
    with virtualenv():
        run("python manage.py collectstatic --noinput")
    print green('- Collectstatic Ok')


def create_super_user():
    """ Create super user in db"""
    with virtualenv():
        run("python manage.py createsuperuser")
    print green('- Create Super user Ok')

###################
# Virtualenv util #
###################
@_contextmanager
def virtualenv():
    """ Wrapper to run commands in the virtual env context """
    with prefix('WORKON_HOME=~/.virtualenvs'):
        with prefix('source ~/.local/bin/virtualenvwrapper.sh'):
            with prefix('workon %s' % env.project_name):
                with cd(env.base_dir):
                    yield
