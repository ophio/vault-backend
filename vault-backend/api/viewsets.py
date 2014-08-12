# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from rest_framework import generics, viewsets, status, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

class UUIDReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'


class UUIDModelViewset(viewsets.ModelViewSet):
    lookup_field = 'id'
