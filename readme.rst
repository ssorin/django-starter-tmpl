===================
 Django Starter Tmpl
===================

This is a simple Django 1.11+ project template with my preferred setup.

Most of my projects are deployed to AlwaysData, so hhe deployment (with fabric) is optimized for that.

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

Requirements
============
- Django>=1.11.0,<1.12.0
- django-sekizai>=0.10,<0.11
- django-extensions>=1.8.0,<1.9.0
- django-debug-toolbar==1.8
- psycopg2==2.6

Getting Started
===============
Development environment
-----------------------
You have 2 choices:
1) with fabric:
    - clone project
    - change git project
    - fab dev deploy / fab dev update

2) with docker:
    - clone project
    - change git project
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
- secret key:
    - Translation
    - Fix issue if secret_key file is empty
    - Test
    - Create a specific App
    - PR on django-extension ?
- fabfile: add try/except + add test
