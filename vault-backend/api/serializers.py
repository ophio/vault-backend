# -*- coding: utf-8 -*-

from rest_framework import serializers

from core.models import Platform, Developer, Library, LibraryVersion

class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Platform
        fields = ('id', 'name')


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = ('id', 'name', 'email')


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ('id', 'name', 'platform', 'link')


class LibraryVersionSerializer(serializers.ModelSerializer):
    library = LibrarySerializer()

    class Meta:
        model = LibraryVersion
        fields = ('id', 'library', 'version', 'link')
