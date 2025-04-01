from rest_framework import renderers


class UnifiedJSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']

        # 如果已经是自定义格式，直接返回
        if isinstance(data, dict) and 'code' in data and 'msg' in data:
            return super().render(data, accepted_media_type, renderer_context)

        # 其他情况强制包装为统一格式
        wrapped_data = {
            "code": 200,  # 默认业务码为200
            "data": data if data is not None else {},
            "msg": "success"
        }
        return super().render(wrapped_data, accepted_media_type, renderer_context)