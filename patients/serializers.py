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
        extra_kwargs = {
            'id': {'read_only': False},  # 允许客户端传入ID
            'archive_id': {'required': True}  # 确保复合主键字段必填
        }

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