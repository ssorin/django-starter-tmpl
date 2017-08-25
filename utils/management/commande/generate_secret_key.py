# -*- coding: utf-8 -*-
"""
Générer une clé secrete avec une commande manage.py:
http://sametmax.com/quelques-outils-pour-gerer-les-cles-secretes-en-django/
"""

from django.core.management.base import BaseCommand, CommandError
 
class Command(BaseCommand):
    help = 'Generate a secret key'
 
    def add_arguments(self, parser):
        parser.add_argument('size', default=50, type=int)
 
    def handle(self, *args, **options):
        self.stdout.write(secret_key(options['size']))
