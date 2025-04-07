from rest_framework import serializers


from .models import Dictionary, DataTemplate, DataTemplateCategory


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
class DataTemplatesSerializer(serializers.ModelSerializer):
    # 定义一个只读字段，用于展示关联的类别名称
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = DataTemplate
        fields = ('id', 'name', 'description', 'category_id', 'category_name', 'used_n')


class DataTemplateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTemplateCategory
        fields = ('id', 'name')