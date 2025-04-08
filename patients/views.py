# patients/jwt_views.py
from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from core.pagination import StandardPagination
from .models import Archive, ArchiveCaseRelative, BaseInfo, Cases, ClinicalInfo, Identity
from .serializers import (
    ArchiveSerializer, ArchiveCaseRelativeSerializer, BaseInfoSerializer,
    CasesSerializer, ClinicalInfoSerializer, IdentitySerializer
)

class ArchiveListCreateView(generics.ListCreateAPIView):
    queryset = Archive.objects.all().order_by('id')  # 必须有序
    serializer_class = ArchiveSerializer
    pagination_class = StandardPagination

class ArchiveDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer

class ArchiveCaseRelativeListCreateView(generics.ListCreateAPIView):
    queryset = ArchiveCaseRelative.objects.all().order_by('id')
    serializer_class = ArchiveCaseRelativeSerializer
    pagination_class = StandardPagination

class ArchiveCaseRelativeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArchiveCaseRelative.objects.all()
    serializer_class = ArchiveCaseRelativeSerializer

# 其他视图类保持相同结构，仅需为ListCreate视图添加分页和排序
class BaseInfoListCreateView(generics.ListCreateAPIView):
    queryset = BaseInfo.objects.all().order_by('id')
    serializer_class = BaseInfoSerializer
    pagination_class = StandardPagination

class CasesListCreateView(generics.ListCreateAPIView):
    queryset = Cases.objects.all().order_by('id')
    serializer_class = CasesSerializer
    pagination_class = StandardPagination

class ClinicalInfoListCreateView(generics.ListCreateAPIView):
    queryset = ClinicalInfo.objects.all().order_by('id')
    serializer_class = ClinicalInfoSerializer
    pagination_class = StandardPagination

class IdentityListCreateView(generics.ListCreateAPIView):
    queryset = Identity.objects.all().order_by('id')
    serializer_class = IdentitySerializer
    pagination_class = StandardPagination

class BaseInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseInfo.objects.all()
    serializer_class = BaseInfoSerializer

class CasesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer

class ClinicalInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClinicalInfo.objects.all()
    serializer_class = ClinicalInfoSerializer

class IdentityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer

class GenderCountView(APIView):
    def get(self, request):
        # 统计男女人数
        gender_count = Identity.objects.values('gender').annotate(count=Count('gender'))
        # 返回的数据格式 {1: 男性人数, 2: 女性人数}
        result = {gender['gender']: gender['count'] for gender in gender_count}
        return Response(result)