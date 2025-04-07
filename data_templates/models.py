from django.db import models

class DataTemplateCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'data_template_category'

    def __str__(self):
        return self.name

class DataTemplate(models.Model):
    id = models.AutoField(primary_key=True)  # 自动增长的主键id
    name = models.CharField(max_length=255, db_comment='模板名称')
    description = models.TextField(blank=True, null=True, db_comment='描述')
    # 指定 db_column 对应数据库中的字段名称
    category = models.ForeignKey(DataTemplateCategory, on_delete=models.CASCADE, db_column='category_id',
                                 verbose_name='类型外键引用')
    used_n = models.IntegerField(db_comment='被使用次数')

    class Meta:
        db_table = 'data_template'
        indexes = [
            models.Index(fields=['name'], name='data_template_name_index'),  # 修改索引名称
        ]

    def __str__(self):
        return self.name



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
