

from .models import DataTemplate



# 系统词条增删改查
from rest_framework import generics
from .models import Dictionary
from .serializers import DictionarySerializer, DataTemplatesSerializer


class DictionaryListCreateView(generics.ListCreateAPIView):
    """获取所有词条 & 创建新词条"""
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

class DictionaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """获取、更新或删除指定 ID 的词条"""
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
# 数据模板增删改查

class DataTemplatesListCreateView(generics.ListCreateAPIView):
    queryset = DataTemplate.objects.all()
    serializer_class = DataTemplatesSerializer

class DataTemplatesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataTemplate.objects.all()
    serializer_class = DataTemplatesSerializer