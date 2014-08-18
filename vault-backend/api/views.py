# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from rest_framework import generics, status, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.db.models import Count

from api.serializers import PlatformSerializer, ProjectSerializer, ProjectCreateSerializer, DeveloperSerializer, LibrarySerializer, LibraryCreateSerializer, LibraryVersionSerializer, LibraryVersionCreateSerializer, PostSerializer, PostCreateSerializer

from api.viewsets import UUIDModelViewset, UUIDReadOnlyModelViewset

from api.filters import PlatformFilterBackend, LibraryFilterBackend, LibraryVersionFilterBackend

from core.models import Platform, Project, Developer, Library, LibraryVersion, Post

from datetime import datetime


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    '''

    List of api endpoints for this Project.

    ### SignUp

    POST at sign-up's url (/api/sign-up/) to register a user.

    payload = {
        "name": "<NAME>",
        "email": "<EMAIL>",
        "password": "<RAW_PASSWORD">
    }

    ### Authentication

    POST at auth-token's url (/api/auth-token/) to obtain a JSON-Web Token. `BasicAuth` is also supported.

    payload = {
        "username": "<EMAIL>",
        "password": "<RAW_PASSWORD">
    }

    ### Errors

    By default all error responses will include a key `details` in the body of
    the response.

    '''
    return Response({
        'api_root': reverse('api_root', request=request, format=format),
        'platforms': reverse('api_platforms-list', request=request, format=format),
        'projects': reverse('api_projects-list', request=request, format=format),
        # 'sign-up': reverse('api_signup', request=request, format=format),
        'developers': reverse('api_developers-list', request=request, format=format),
        'libraries': reverse('api_libraries-list', request=request, format=format),
        'versions': reverse('api_versions-list', request=request, format=format),
        'posts': reverse('api_posts-list', request=request, format=format),
    })

class PlatformViewSet(UUIDReadOnlyModelViewset):
    '''
    ### List of available platforms on Vault.

    ## Paginated Call

    response = {
        "count": "<TOTAL_COUNT>"
        "next": "<NEXT_PAGE_URL>"
        "previous": "<PREVIOUS_PAGE_URL>"
        "results": "<OBJECTS>"
    }

    '''
    model = Platform
    serializer_class = PlatformSerializer
    permission_classes = ((permissions.AllowAny),)
    paginate_by = 20

class ProjectViewSet(UUIDModelViewset):
    '''
    ### List of available Projects on Vault.

    ## Paginated Call

    response = {
        "count": "<TOTAL_COUNT>"
        "next": "<NEXT_PAGE_URL>"
        "previous": "<PREVIOUS_PAGE_URL>"
        "results": "<OBJECTS>"
    }

    '''
    model = Project
    serializer_class = ProjectSerializer
    permission_classes = ((permissions.AllowAny),)
    filter_backends = (PlatformFilterBackend,)
    paginate_by = 20

    def create(self, request, *args, **kwargs):
        self.serializer_class = ProjectCreateSerializer
        return super(ProjectViewSet, self).create(request, *args, **kwargs)

class DeveloperViewSet(UUIDReadOnlyModelViewset):
    model = Developer
    serializer_class = DeveloperSerializer
    permission_classes = ((permissions.AllowAny),)
    paginate_by = 20


class LibraryViewSet(UUIDModelViewset):
    model = Library
    serializer_class = LibrarySerializer
    permission_classes = ((permissions.AllowAny),)
    filter_backends = (PlatformFilterBackend,)
    paginate_by = 20

    def create(self, request, *args, **kwargs):
        self.serializer_class = LibraryCreateSerializer
        return super(LibraryViewSet, self).create(request, *args, **kwargs)


class LibraryVersionViewSet(UUIDModelViewset):
    model = LibraryVersion
    serializer_class = LibraryVersionSerializer
    permission_classes = ((permissions.AllowAny),)
    filter_backends = (PlatformFilterBackend, LibraryFilterBackend)
    paginate_by = 20

    def create(self, request, *args, **kwargs):
        self.serializer_class = LibraryVersionCreateSerializer
        return super(LibraryVersionViewSet, self).create(request, *args, **kwargs)


class PostViewSet(UUIDModelViewset):
    model = Post
    serializer_class = PostSerializer
    permission_classes = ((permissions.AllowAny),)
    filter_backends = (PlatformFilterBackend, LibraryFilterBackend, LibraryVersionFilterBackend)
    paginate_by = 20

    def create(self, request, *args, **kwargs):
        self.serializer_class = PostCreateSerializer
        return super(PostViewSet, self).create(request, *args, **kwargs)
