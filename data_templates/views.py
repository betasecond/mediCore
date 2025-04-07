from rest_framework import generics
from .models import Dictionary, DataTemplate, DataTemplateCategory
from .serializers import DictionarySerializer, DataTemplatesSerializer, DataTemplateCategorySerializer


# -------------------------------
# 系统词条（Dictionary）的增删改查接口
# -------------------------------

class DictionaryListCreateView(generics.ListCreateAPIView):
    """
    获取所有词条 & 创建新词条
    GET: 查询所有词条
    POST: 创建新词条
    """
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

class DictionaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    获取、更新或删除指定 ID 的词条
    GET: 查询指定词条详情
    PUT/PATCH: 更新词条
    DELETE: 删除词条
    """
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

# -------------------------------
# 数据模板（DataTemplate）的增删改查接口
# -------------------------------

class DataTemplatesListCreateView(generics.ListCreateAPIView):
    """
    获取所有数据模板 & 创建新数据模板
    GET: 查询所有数据模板（自动联查关联的类别名称）
    POST: 创建新数据模板
    """
    # 使用 select_related 优化外键关联查询，减少数据库查询次数
    queryset = DataTemplate.objects.select_related('category').all()
    serializer_class = DataTemplatesSerializer

class DataTemplatesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    获取、更新或删除指定 ID 的数据模板
    GET: 查询指定数据模板详情（包括关联的类别名称）
    PUT/PATCH: 更新数据模板
    DELETE: 删除数据模板
    """
    queryset = DataTemplate.objects.select_related('category').all()
    serializer_class = DataTemplatesSerializer
# -------------------------------
# 数据模板分类（DataTemplateCategory）的增删改查接口
# -------------------------------

class DataTemplateCategoryListCreateView(generics.ListCreateAPIView):
    """
    GET: 获取所有分类
    POST: 创建新分类
    """
    queryset = DataTemplateCategory.objects.all()
    serializer_class = DataTemplateCategorySerializer

class DataTemplateCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: 获取指定分类详情
    PUT/PATCH: 更新指定分类
    DELETE: 删除指定分类
    """
    queryset = DataTemplateCategory.objects.all()
    serializer_class = DataTemplateCategorySerializer