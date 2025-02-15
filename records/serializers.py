# records/serializers.py
from rest_framework import serializers
from .models import DataTable, ExaminationImages, ExaminationSheet, TestingSheet, DocumentChart, Documents, Image, Shape, Text

class DataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTable
        fields = '__all__'

class ExaminationImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExaminationImages
        fields = '__all__'

class ExaminationSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExaminationSheet
        fields = '__all__'

class TestingSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingSheet
        fields = '__all__'

class DocumentChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentChart
        fields = '__all__'

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = '__all__'

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'