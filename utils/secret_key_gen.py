# -*- coding: utf-8 -*-
"""
On ne veut pas mettre sa SECRET_KEY en prod, et utiliser un service pour générer la clé, ça va deux minutes.
Le but de cette dernière est d’avoir ça dans son fichier de settings:

SECRET_KEY = get_secret_key('secret_key')

Et de foutre ‘secret_key’ dans son .gitignore.

Comme ça:
Si on n’a pas de clé secrète, on en génère une.
Si on a une, elle est dans un fichier qui n’est PAS dans settings.py.
On peut commiter settings.py. Chaque env de dev et prod a sa clé secrète automatiquement.
On peut overrider la clé avec une variable d’environnement si on le souhaite.

http://sametmax.com/quelques-outils-pour-gerer-les-cles-secretes-en-django/
"""

import random
import string
import io
import os
 
try:
    import pwd
except ImportError:
    pass
 
try:
    import grp
except ImportError:
    pass

def secret_key(size=50):
    """
        Générer une clé secrète:
    """
    pool = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.SystemRandom().choice(pool) for i in range(size))
 
def secret_key_from_file(
        file_path, 
        create=True, 
        size=50, 
        file_perms=None, # unix uniquement
        file_user=None, # unix uniquement
        file_group=None # unix uniquement
    ):
    """
        Une fonction pour lire la clé depuis un fichier texte ou générer la clé si elle n’existe pas:
    """
    # todo : tester si secret_key est vide ou non
    try:
        with io.open(file_path) as f:
            return f.read().strip()
    except IOError as e:
        if e.errno == 2 and create:
            with io.open(file_path, 'w') as f:
                key = secret_key(size)
                f.write(unicode(key))
 
            if any((file_perms, file_user, file_group)) and not pwd:
                raise ValueError('File chmod and chown are for Unix only')
 
            if file_user:
                os.chown(file_path, uid=pwd.getpwnam(file_user).pw_uid)
 
            if file_group:
                os.chown(file_path, gid=grp.getgrnam(file_group).gr_gid)
 
            if file_perms:
                os.chmod(file_path, int(str(file_perms), 8))
 
            return key
 
        raise

def get_secret_key(
        file_path=None, 
        create=True, 
        size=50, 
        file_perms=None, 
        file_user=None, 
        file_group=None,
        env_var="DJANGO_SECRET_KEY"
    ):
    """
        Et une fonction pour récupérer la clé depuis une variable d’environnement ou un fichier
    """
    try:
        return os.environ[env_var]
    except KeyError:
        if file_path:
            return secret_key_from_file(file_path, create=create, size=size)
        raise
