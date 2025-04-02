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
    data_template_id = models.IntegerField(db_comment='模板外键')
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
    id = models.AutoField(primary_key=True)  # 增加自动增长的主键id
    word_code = models.CharField(max_length=255, unique=True, db_comment='词条编号')
    word_name = models.CharField(max_length=255, db_comment='中文名称')
    word_eng = models.CharField(max_length=255, blank=True, null=True, db_comment='英文名称')
    word_short = models.CharField(max_length=255, blank=True, null=True, db_comment='英文缩写')
    word_class = models.CharField(max_length=255, db_comment='词条类型')
    word_apply = models.CharField(max_length=255, db_comment='词条应用')
    word_belong = models.CharField(max_length=255, blank=True, null=True, db_comment='从属别名')

    class Meta:
        db_table = 'dictionary'
        indexes = [
            models.Index(fields=['word_name'], name='name_index'),
        ]

    def __str__(self):
        return self.word_name
