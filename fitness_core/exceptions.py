from rest_framework.exceptions import APIException


class InvalidPageSizeException(APIException):
    status_code = 400
    default_detail = "invalid-page-size."
    default_code = "invalid_page_size"
