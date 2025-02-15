from django.db import models

# Create your models here.
class DataTable(models.Model):
    id = models.IntegerField(primary_key=True)
    case_id = models.IntegerField(db_comment='病历外键引用')
    table_name = models.CharField(max_length=255)
    data_template_id = models.IntegerField(db_comment='引用数�\x8d�模�\x9d�外键')

    class Meta:
        managed = False
        db_table = 'data_table'

class ExaminationImages(models.Model):
    id = models.IntegerField(primary_key=True)
    examination_sheet_id = models.IntegerField(db_comment='检查表外键引用')
    url = models.CharField(max_length=255)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examination_images'


class ExaminationSheet(models.Model):
    id = models.IntegerField(primary_key=True)
    data_table_id = models.IntegerField(db_comment='数�\x8d�表外键引用')
    case_id = models.IntegerField(blank=True, null=True, db_comment='病历冗余�\xad�储')
    name = models.CharField(max_length=255)
    name_code = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    category_code = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255, db_comment='诊�\xad')
    description = models.CharField(max_length=255, blank=True, null=True, db_comment='检查�\x8f\x8f述')
    exam_date = models.DateTimeField()
    inspector = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examination_sheet'

class TestingSheet(models.Model):
    id = models.IntegerField(primary_key=True)
    data_table_id = models.IntegerField(db_comment='数�\x8d�表外键引用')
    case_id = models.IntegerField(blank=True, null=True, db_comment='病历冗余�\xad�储')
    name = models.CharField(max_length=255)
    name_code = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)
    name_short = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    category_code = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    type_code = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    test_date = models.DateTimeField()
    inspector = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_sheet'


class DocumentChart(models.Model):
    id = models.IntegerField(primary_key=True)
    document_id = models.IntegerField()
    chart_id = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()

    class Meta:
        managed = False
        db_table = 'document_chart'


class Documents(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    properties = models.CharField(max_length=255, db_comment='属性，�\xad�JSON')

    class Meta:
        managed = False
        db_table = 'documents'

class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    document_id = models.IntegerField(db_comment='文档引用')
    url = models.CharField(max_length=255)
    remark = models.CharField(max_length=255, blank=True, null=True)
    x = models.FloatField()
    y = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    is_stroke = models.IntegerField()
    stroke_weight = models.FloatField(db_comment='�\x8f\x8f边粗细')
    stroke_color = models.CharField(max_length=255, db_comment='�\x8f\x8f边颜色')

    class Meta:
        managed = False
        db_table = 'image'


class Shape(models.Model):
    id = models.IntegerField(primary_key=True)
    document_id = models.IntegerField(db_comment='文档引用')
    x = models.FloatField()
    y = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    is_fill = models.IntegerField()
    fill_color = models.CharField(max_length=255, db_comment='填充颜色')
    is_stroke = models.IntegerField()
    stroke_color = models.CharField(max_length=255, db_comment='�\x8f\x8f边颜色')
    path = models.CharField(max_length=255, db_comment='点集，�\xad�JSON')

    class Meta:
        managed = False
        db_table = 'shape'




class Text(models.Model):
    id = models.IntegerField(primary_key=True)
    document_id = models.IntegerField(db_comment='文档引用')
    x = models.FloatField()
    y = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    family = models.CharField(max_length=255)
    size = models.IntegerField()
    color = models.CharField(max_length=255)
    weight = models.IntegerField()
    underline = models.IntegerField()
    slope = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'text'