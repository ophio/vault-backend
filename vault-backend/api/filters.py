from rest_framework import filters
from core.models import Platform

class LibraryFilterBackend(filters.BaseFilterBackend):
    """
    Filter that libraries to be filtered by their platform
    """
    def filter_queryset(self, request, queryset, view):
        platform_name = request.QUERY_PARAMS.get('platform', None)
        query_string = request.QUERY_PARAMS.get('query', None)

        if platform_name is not None:
            try:
                platform = Platform.objects.get(name__iexact=platform_name)
                queryset = queryset.filter(platform=platform)
            except Platform.DoesNotExist:
                pass

        if query_string is not None:
            queryset = queryset.filter(name__icontains=query_string)
        else:
            queryset = queryset.none()

        return queryset
