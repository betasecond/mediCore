
from .models import AnalysisSheet

# 分析表增删改查
from rest_framework import generics

from .serializers import AnalysisSheetSerializer


class AnalysisSheetListCreateView(generics.ListCreateAPIView):
    """获取所有分析表 & 创建分析表"""
    queryset = AnalysisSheet.objects.all()
    serializer_class = AnalysisSheetSerializer

class AnalysisSheetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """获取、更新或删除指定 ID 的分析表"""
    queryset = AnalysisSheet.objects.all()
    serializer_class = AnalysisSheetSerializer

