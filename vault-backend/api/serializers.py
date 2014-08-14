# -*- coding: utf-8 -*-

from rest_framework import serializers

from core.models import Platform, Developer, Project, Library, LibraryVersion, Post

class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Platform
        fields = ('id', 'name')


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = ('id', 'name', 'email')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name')


class LibrarySerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()

    class Meta:
        model = Library
        fields = ('id', 'name', 'platform', 'link')

class LibraryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ('id', 'name', 'platform', 'link')


class LibraryVersionSerializer(serializers.ModelSerializer):
    library = LibrarySerializer()

    class Meta:
        model = LibraryVersion
        fields = ('id', 'library', 'version', 'link')


class LibraryVersionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryVersion
        fields = ('id', 'library', 'version', 'link')


class PostSerializer(serializers.ModelSerializer):
    library = LibraryVersionSerializer()
    developer = DeveloperSerializer()
    project = ProjectSerializer()

    class Meta:
        model = Post
        fields = ('id', 'library', 'description', 'developer', 'project')


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'library', 'description', 'developer', 'project')
