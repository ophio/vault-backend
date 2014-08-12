# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from api.views import PlatformViewSet, DeveloperViewSet, LibraryViewSet, LibraryVersionViewSet

# Wire up our API using automatic URL routing.
# Additionally, include login URLs for the browseable API.
urlpatterns = format_suffix_patterns(patterns('api.views',
    url(r'^$', 'api_root', name='api_root'),
))

urlpatterns += patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth-token/', 'rest_framework_jwt.views.obtain_jwt_token', name='api_auth_token'),
)

router = DefaultRouter()
router.register(r'platforms', PlatformViewSet, base_name='api_platforms')
router.register(r'developers', DeveloperViewSet, base_name='api_developers')
router.register(r'libraries', LibraryViewSet, base_name='api_libraries')
router.register(r'versions', LibraryVersionViewSet, base_name='api_versions')

urlpatterns += router.urls
