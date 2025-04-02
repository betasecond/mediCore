from rest_framework import serializers

import data_templates
from .models import Dictionary

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
class DataTemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_templates
        fields = '__all__'
