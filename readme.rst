===================
 Django Starter Tmpl
===================

This is a simple Django 1.11+ project template with my preferred setup.

Fabric deployment is optimized for AlwaysData

Features
===============
- Django 1.11
- Settings ready for Development.
- Docker for development.
- Deployment ready for AlwaysData with Fabric
- Automatic settings for Staging and Production with Fabric
- Automatic secret key
- Debug information with django-debug-toolbar.
- Collection of custom extensions with django-extensions.
- PostgreSQL database support with psycopg2.
- livereload: Application performing a LiveReload with tiny-lr once the development server is ready (https://github.com/Fantomas42/django-livereload).

Requirements
============
- Django>=1.11.0,<1.12.0
- django-sekizai>=0.10,<0.11
- django-extensions>=1.8.0,<1.9.0
- django-debug-toolbar==1.8
- psycopg2==2.6dea
- livereload

Getting Started
===============
Development environment
-----------------------
2 choices:

1) with fabric:
    - clone project
    - change git remote origin
    - fab dev deploy / fab dev update

2) with docker:
    - clone project
    - change git remote origin
    - run: docker-compose build
    - run: docker-compose up

Staging environment
-------------------
- clone project
- fab staging deploy / fab staging update

Production environment
----------------------
- clone project
- fab prod deploy / fab prod update

Todo
====
- secret key: utils/readme.rst
- fabfile: test
