import json
import uuid

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from .models import DataTemplate, Dictionary
from .serializers import DictionarySerializer

from drf_yasg.utils import swagger_auto_schema

class DataTemplateListView(View):
    @swagger_auto_schema(operation_description="获取所有数据模板")
    def get(self, request, *args, **kwargs):
        data_templates = DataTemplate.objects.all().values()
        return JsonResponse(list(data_templates), safe=False)

class DataTemplateDetailView(View):
    @swagger_auto_schema(operation_description="获取指定ID的数据模板")
    def get(self, request, pk, *args, **kwargs):
        data_template = get_object_or_404(DataTemplate, pk=pk)
        return JsonResponse({
            'id': data_template.id,
            'name': data_template.name,
            'description': data_template.description,
            'category_id': data_template.category_id,
            'used_n': data_template.used_n
        })

class DataTemplateCreateView(View):
    @swagger_auto_schema(operation_description="创建新的数据模板")
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        data_template = DataTemplate.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            category_id=data.get('category_id'),
            used_n=data.get('used_n')
        )
        return JsonResponse({
            'id': data_template.id,
            'name': data_template.name,
            'description': data_template.description,
            'category_id': data_template.category_id,
            'used_n': data_template.used_n
        }, status=201)

class DataTemplateUpdateView(View):
    @swagger_auto_schema(operation_description="更新指定ID的数据模板")
    def post(self, request, pk, *args, **kwargs):
        data_template = get_object_or_404(DataTemplate, pk=pk)
        data = json.loads(request.body)
        data_template.name = data.get('name')
        data_template.description = data.get('description')
        data_template.category_id = data.get('category_id')
        data_template.used_n = data.get('used_n')
        data_template.save()
        return JsonResponse({
            'id': data_template.id,
            'name': data_template.name,
            'description': data_template.description,
            'category_id': data_template.category_id,
            'used_n': data_template.used_n
        })

class DataTemplateDeleteView(View):
    @swagger_auto_schema(operation_description="删除指定ID的数据模板")
    def post(self, request, pk, *args, **kwargs):
        data_template = get_object_or_404(DataTemplate, pk=pk)
        data_template.delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=204)

# 系统词条增删改查
from rest_framework import generics
from .models import Dictionary
from .serializers import DictionarySerializer

class DictionaryListCreateView(generics.ListCreateAPIView):
    """获取所有词条 & 创建新词条"""
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

class DictionaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """获取、更新或删除指定 ID 的词条"""
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
