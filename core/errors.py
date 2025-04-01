# myapp/errors.py

from rest_framework.exceptions import APIException

class CustomError(APIException):
    status_code = 400
    default_detail = 'An error occurred.'
    default_code = 'custom_error'

class InvalidDataError(CustomError):
    status_code = 400
    default_detail = 'Invalid data provided.'
    default_code = 'invalid_data'

class PermissionDeniedError(CustomError):
    status_code = 403
    default_detail = 'Permission denied.'
    default_code = 'permission_denied'
