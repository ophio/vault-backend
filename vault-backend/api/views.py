# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from rest_framework import generics, viewsets, status, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.db.models import Count

from api.serializers import PlatformSerializer

from core.models import Platform

from datetime import datetime


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    '''

    List of api endpoints for this Project.

    ### Authentication

    Visit auth-token's url to obtain a JSON-Web Token. `BasicAuth` is also supported.

    ### Errors

    By default all error responses will include a key `details` in the body of
    the response.

    '''
    return Response({
        'api_root': reverse('api_root', request=request, format=format),
        'platforms': reverse('api_platforms-list', request=request, format=format),
    })



class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Endpoint to get and update profile of a `User`.
    '''
    model = Platform
    serializer_class = PlatformSerializer
    permission_classes = ((permissions.AllowAny),)
