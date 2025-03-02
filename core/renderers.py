from rest_framework import renderers


class UnifiedJSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']

        # 如果已经处理过异常，直接返回数据
        if isinstance(data, dict) and 'code' in data and 'msg' in data:
            return super().render(data, accepted_media_type, renderer_context)

        # 包装标准结构
        wrapped_data = {
            "code": response.status_code,
            "data": data if data is not None else {},
            "msg": "success" if 200 <= response.status_code < 300 else "error"
        }
        return super().render(wrapped_data, accepted_media_type, renderer_context)