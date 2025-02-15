from django.db import models

# Create your models here.
class DataTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category_id = models.IntegerField(db_comment='类型外键引用')
    used_n = models.IntegerField(db_comment='被使用次数')

    class Meta:
        managed = False
        db_table = 'data_template'


class DataTemplateCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'data_template_category'


class DataTemplateDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    data_template_id = models.IntegerField(db_comment='模�\x9d�外键')
    item_name = models.CharField(max_length=255)
    item_name_code = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)
    category_name_code = models.CharField(max_length=255)
    type_name = models.CharField(max_length=255)
    type_name_code = models.CharField(max_length=255)
    order_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_template_details'


class DataTemplateTags(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'data_template_tags'


class DataTemplateTagsRelative(models.Model):
    id = models.IntegerField(primary_key=True)
    template_id = models.IntegerField()
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_template_tags_relative'


class Dictionary(models.Model):
    word_code = models.CharField(max_length=255, db_comment='�\x8d�\x9d�编�\x8f�')
    word_name = models.CharField(max_length=255, db_comment='�\xad文�\x90\x8d称')
    word_eng = models.CharField(max_length=255, blank=True, null=True, db_comment='英文�\x90\x8d称')
    word_short = models.CharField(max_length=255, blank=True, null=True, db_comment='英文缩写')
    word_class = models.CharField(max_length=255, db_comment='�\x8d�\x9d�类型')
    word_apply = models.CharField(max_length=255, db_comment='�\x8d�\x9d�应用')
    word_belong = models.CharField(max_length=255, blank=True, null=True, db_comment='从属别�\x90\x8d')

    class Meta:
        managed = False
        db_table = 'dictionary'
        unique_together = (('id', 'word_code'),)

