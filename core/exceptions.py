from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    # 获取标准响应
    response = exception_handler(exc, context)

    # 处理已知的DRF异常
    if response is not None:
        error_msg = ""
        # 提取DRF内置异常的消息
        if hasattr(exc, 'detail') and isinstance(exc.detail, (str, dict, list)):
            error_msg = exc.detail
        elif hasattr(exc, 'get_full_details'):
            error_msg = exc.get_full_details()
        else:
            error_msg = str(exc)

        # 统一错误格式（保持data为null）
        response.data = {
            "code": response.status_code,
            "data": "",
            "msg": error_msg
        }

    # 处理未捕获的异常
    else:
        response = Response(
            data={
                "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "data": "",
                "msg": f"Server Error: {str(exc)}"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response