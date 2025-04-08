from django.db import models
from utils.snowflake import Snowflake

snowflake = Snowflake(datacenter_id=1, worker_id=1)

def generate_snowflake_id():
    return snowflake.get_id()

# Create your models here.
class Archive(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, arcive_id) found, that is not supported. The first column is selected.
    arcive_id = models.CharField(max_length=255)
    archive_name = models.CharField(max_length=255, db_comment='专病档案名称')
    description = models.TextField(blank=True, null=True, db_comment='专病档案说明')

    class Meta:
        managed = False
        db_table = 'archive'
        unique_together = (('id', 'arcive_id'),)


class ArchiveCaseRelative(models.Model):
    id = models.IntegerField(primary_key=True)
    archive_id = models.CharField(max_length=255)
    case_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'archive_case_relative'


class BaseInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    case_id = models.CharField(max_length=255, db_comment='病历外键引用')
    name = models.CharField(max_length=255)
    name_code = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    category_code = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    type_code = models.CharField(max_length=255)
    value = models.CharField(max_length=255, db_comment='值')

    class Meta:
        managed = False
        db_table = 'base_info'


class Cases(models.Model):
    id = models.BigIntegerField(primary_key=True, default=generate_snowflake_id, editable=False)
    case_id = models.CharField(max_length=255)
    identity_id = models.CharField(max_length=255)
    inhospital_id = models.CharField(max_length=255, blank=True, null=True, db_comment='住院')

    class Meta:
        managed = False
        db_table = 'cases'
        unique_together = (('id', 'case_id'),)




class ClinicalInfo(models.Model):
    name = models.CharField(max_length=255)
    name_code = models.CharField(max_length=255)
    case_id = models.CharField(max_length=255, db_comment='病例外键')

    class Meta:
        managed = False
        db_table = 'clinical_info'












class Identity(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, identity_id) found, that is not supported. The first column is selected.
    identity_id = models.CharField(unique=True, max_length=255, db_comment='身份证')
    true_name = models.CharField(max_length=255, db_comment='真实姓名')
    gender = models.IntegerField(db_comment='性别')
    birth_date = models.DateTimeField(db_comment='出生年月日')

    class Meta:
        managed = False
        db_table = 'identity'
        unique_together = (('id', 'identity_id'),)

