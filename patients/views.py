from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Archive, ArchiveCaseRelative, BaseInfo, Cases, ClinicalInfo, Identity
from .serializers import (
    ArchiveSerializer, ArchiveCaseRelativeSerializer, BaseInfoSerializer,
    CasesSerializer, ClinicalInfoSerializer, IdentitySerializer
)

class ArchiveListCreateView(generics.ListCreateAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer

class ArchiveDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer

class ArchiveCaseRelativeListCreateView(generics.ListCreateAPIView):
    queryset = ArchiveCaseRelative.objects.all()
    serializer_class = ArchiveCaseRelativeSerializer

class ArchiveCaseRelativeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArchiveCaseRelative.objects.all()
    serializer_class = ArchiveCaseRelativeSerializer

class BaseInfoListCreateView(generics.ListCreateAPIView):
    queryset = BaseInfo.objects.all()
    serializer_class = BaseInfoSerializer

class BaseInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseInfo.objects.all()
    serializer_class = BaseInfoSerializer

class CasesListCreateView(generics.ListCreateAPIView):
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer

class CasesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer

class ClinicalInfoListCreateView(generics.ListCreateAPIView):
    queryset = ClinicalInfo.objects.all()
    serializer_class = ClinicalInfoSerializer

class ClinicalInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClinicalInfo.objects.all()
    serializer_class = ClinicalInfoSerializer

class IdentityListCreateView(generics.ListCreateAPIView):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer

class IdentityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer