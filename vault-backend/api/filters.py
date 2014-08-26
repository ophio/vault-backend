from rest_framework import filters
from core.models import Platform, Library, LibraryVersion, Developer, Project

class PlatformFilterBackend(filters.BaseFilterBackend):
    """
    Filter that filters objects based on their platform
    """
    def filter_queryset(self, request, queryset, view):
        view_model_name = view.model.__name__
        platform_id = request.QUERY_PARAMS.get('platform', None)
        query_string = request.QUERY_PARAMS.get('query', None)

        if platform_id is not None:
            try:
                platform = Platform.objects.get(id=platform_id)
                if view_model_name in ['Library', 'Project']:
                    queryset = queryset.filter(platform=platform)
                if view_model_name == 'LibraryVersion':
                    queryset = queryset.filter(library__platform=platform)
                if view_model_name == 'Post':
                    queryset = queryset.filter(library__library__platform=platform)
            except Platform.DoesNotExist:
                return queryset.none()

        if query_string is not None:
            if view_model_name in ['Library', 'Project']:
                queryset = queryset.filter(name__icontains=query_string)

        return queryset

class LibraryFilterBackend(filters.BaseFilterBackend):
    """
    Filter that filters objects based on their Library
    """
    def filter_queryset(self, request, queryset, view):
        view_model_name = view.model.__name__
        library_id = request.QUERY_PARAMS.get('library', None)

        if library_id is not None:
            try:
                library = Library.objects.get(id=library_id)
                if view_model_name == 'LibraryVersion':
                    queryset = queryset.filter(library=library)
                if view_model_name == 'Post':
                    queryset = queryset.filter(library__library=library)
            except Library.DoesNotExist:
                return queryset.none()

        return queryset

class LibraryVersionFilterBackend(filters.BaseFilterBackend):
    """
    Filter that filters objects based on their LibraryVersion
    """
    def filter_queryset(self, request, queryset, view):
        view_model_name = view.model.__name__
        version_id = request.QUERY_PARAMS.get('version', None)

        if version_id is not None:
            try:
                version = LibraryVersion.objects.get(id=version_id)
                if view_model_name == 'Post':
                    queryset = queryset.filter(library=version)
            except LibraryVersion.DoesNotExist:
                return queryset.none()

        return queryset

class DeveloperFilterBackend(filters.BaseFilterBackend):
    """
    Filter that filters objects based on their Developer
    """
    def filter_queryset(self, request, queryset, view):
        view_model_name = view.model.__name__
        developer_id = request.QUERY_PARAMS.get('developer', None)

        if developer_id is not None:
            try:
                developer = Developer.objects.get(id=developer_id)
                queryset = queryset.filter(developer=developer)
            except Developer.DoesNotExist:
                return queryset.none()

        return queryset

class ProjectFilterBackend(filters.BaseFilterBackend):
    """
    Filter that filters objects based on their Project
    """
    def filter_queryset(self, request, queryset, view):
        view_model_name = view.model.__name__
        project_id = request.QUERY_PARAMS.get('project', None)

        if project_id is not None:
            try:
                project = Project.objects.get(id=project_id)
                queryset = queryset.filter(project=project)
            except Project.DoesNotExist:
                return queryset.none()

        return queryset
