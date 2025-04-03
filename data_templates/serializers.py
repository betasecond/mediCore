from rest_framework import serializers


from .models import Dictionary,DataTemplate

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
class DataTemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTemplate
        fields = '__all__'
