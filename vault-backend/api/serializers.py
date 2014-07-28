# -*- coding: utf-8 -*-

from rest_framework import serializers

from core.models import Platform

class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Platform
        fields = ('id', 'name')
