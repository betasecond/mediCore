from rest_framework import serializers


from .models import Dictionary, DataTemplate, DataTemplateCategory


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
class DataTemplatesSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=DataTemplateCategory.objects.all(),
        source='category',
        write_only=True
    )
    category_name = serializers.CharField(source='category.name', read_only=True)
    # used_n 作为只读字段：不在请求中体现，只在响应中返回
    used_n = serializers.IntegerField(read_only=True)
    id = serializers.CharField()  # 强制将 ID 作为字符串返回 解决精度丢失问题(实际返回和swagger界面显示的id不一致问题)
    class Meta:
        model = DataTemplate
        fields = ('id', 'name', 'description', 'category_id', 'category_name', 'used_n')


class DataTemplateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTemplateCategory
        fields = ('id', 'name')