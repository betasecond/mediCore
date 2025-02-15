from rest_framework import serializers
from .models import Archive, ArchiveCaseRelative, BaseInfo, Cases, ClinicalInfo, Identity

class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = '__all__'

class ArchiveCaseRelativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveCaseRelative
        fields = '__all__'

class BaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseInfo
        fields = '__all__'

class CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cases
        fields = '__all__'

class ClinicalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalInfo
        fields = '__all__'

class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields = '__all__'