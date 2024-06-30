from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 10
    max_page_size = 10
