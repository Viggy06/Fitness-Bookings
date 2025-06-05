from rest_framework import pagination

from .exceptions import InvalidPageSizeException

class CustomPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 150
    page_query_param = "page"

    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size(request)

        try:
            page_size_int = int(page_size)
            if page_size_int < 1:
                raise InvalidPageSizeException
            self.page_size = page_size_int
        except ValueError:
            raise InvalidPageSizeException

        return super().paginate_queryset(queryset, request, view)
