# -*- coding: utf-8 -*-
'''Celery Worker Configuration to autodiscover tasks in all the django apps.

see: http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html
'''
from __future__ import absolute_import

import os
from os.path import dirname
import sys

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.development')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

from configurations import importer
importer.install()

app = Celery('vault-backend')
app.config_from_object(settings)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
