from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            "list": data if data is not None else [],
            "total": self.page.paginator.count,
            "page": self.page.number,
            "page_size": self.page.paginator.per_page
        })