# -*- coding: utf-8 -*-
'''
Pages App Routing.

Handles the top level site pages. You would probably like to add the pages like
homepage, about, terms and conditions, etc. in this app.
'''
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Top Level Pages
# ==============================================================================
urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),
)