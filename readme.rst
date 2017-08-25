===================
 Django Starter Tmpl
===================

This is a simple Django 1.11+ project template with my preferred setup.
Most of my projects are deployed to AlwaysData, so hhe deployment (with fabric) is optimized for that

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

How to install
==============

Todo
====
- secret key:  -- Translation
               -- Fix issue if secret_key file is empty
               -- Test
               -- Create a specific App
               -- PR on django-extension ?

Requirements
============
- Django>=1.11.0,<1.12.0
- django-sekizai>=0.10,<0.11
- django-extensions>=1.8.0,<1.9.0
- django-debug-toolbar==1.8
- psycopg2==2.6

Etape necessaire (à automatiser)
================
1 - clone
2 - rename depot / project
3 - settings/env à définir
4 - définir venv path sur serveur staging / prod
5 - definir setting db + mail sur serveur staging / prod
6 - migrate
7 - (create super user)
8 - collectstatic


Getting Started
===============
EN DEV
- clone project
- change git project
- docker-compose build
- docker-compose up

EN PROD / Stage
- clone project
- run fabfile