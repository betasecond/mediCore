from rest_framework import serializers

from .models import AnalysisSheet

class AnalysisSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisSheet
        fields = '__all__'

