from rest_framework import filters
from core.models import Platform, Library, LibraryVersion

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
