from django.shortcuts import render

# Create your views here.
# records/views.py
from rest_framework import generics
from .models import DataTable, ExaminationImages, ExaminationSheet, TestingSheet, DocumentChart, Documents, Image, Shape, Text
from .serializers import (
    DataTableSerializer, ExaminationImagesSerializer, ExaminationSheetSerializer,
    TestingSheetSerializer, DocumentChartSerializer, DocumentsSerializer,
    ImageSerializer, ShapeSerializer, TextSerializer
)

class DataTableListCreateView(generics.ListCreateAPIView):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer

class DataTableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer

class ExaminationImagesListCreateView(generics.ListCreateAPIView):
    queryset = ExaminationImages.objects.all()
    serializer_class = ExaminationImagesSerializer

class ExaminationImagesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExaminationImages.objects.all()
    serializer_class = ExaminationImagesSerializer

class ExaminationSheetListCreateView(generics.ListCreateAPIView):
    queryset = ExaminationSheet.objects.all()
    serializer_class = ExaminationSheetSerializer

class ExaminationSheetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExaminationSheet.objects.all()
    serializer_class = ExaminationSheetSerializer

class TestingSheetListCreateView(generics.ListCreateAPIView):
    queryset = TestingSheet.objects.all()
    serializer_class = TestingSheetSerializer

class TestingSheetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestingSheet.objects.all()
    serializer_class = TestingSheetSerializer

class DocumentChartListCreateView(generics.ListCreateAPIView):
    queryset = DocumentChart.objects.all()
    serializer_class = DocumentChartSerializer

class DocumentChartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentChart.objects.all()
    serializer_class = DocumentChartSerializer

class DocumentsListCreateView(generics.ListCreateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

class DocumentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ShapeListCreateView(generics.ListCreateAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer

class ShapeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer

class TextListCreateView(generics.ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

class TextDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer