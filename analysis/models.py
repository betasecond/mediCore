from django.db import models

# Create your models here.
# class AnalysisSheet(models.Model):
#     id = models.IntegerField(primary_key=True)
#     analysis_table = models.ForeignKey('AnalysisTable', models.DO_NOTHING, db_comment='分析表引用外键')
#     sheet_code = models.CharField(max_length=255, db_comment='随机生成')
#     sheet_name = models.CharField(max_length=255)
#     remark = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'analysis_sheet'



class AnalysisSheet(models.Model):
    id = models.AutoField(primary_key=True)  # 自动增长的主键id
    analysis_table_id = models.IntegerField(db_comment='分析表引用外键')  # 外键引用（根据需要可做外键关联）
    sheet_code = models.CharField(max_length=255, db_comment='随机生成')  # 随机生成的sheet code
    sheet_name = models.CharField(max_length=255, db_comment='sheet名称')  # sheet名称
    remark = models.CharField(max_length=255, blank=True, null=True, db_comment='备注')  # 备注，允许为空

    class Meta:
        db_table = 'analysis_sheet'
        indexes = [
            models.Index(fields=['sheet_name'], name='sheet_name_index'),  # 创建sheet_name索引
        ]

    def __str__(self):
        return self.sheet_name

class AnalysisSheetDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    analysis_sheet = models.ForeignKey(AnalysisSheet, models.DO_NOTHING)
    case_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_value = models.CharField(max_length=255)
    item_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'analysis_sheet_detail'


class AnalysisTable(models.Model):
    id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    extract_cases = models.CharField(max_length=255)
    since_start = models.DateField()
    since_end = models.DateField()
    data_template_id = models.IntegerField()
    constraint = models.CharField(max_length=255, blank=True, null=True, db_comment='约束条件')
    load_times = models.DateTimeField(blank=True, null=True, db_comment='数据加载次数')
    last_load_date = models.DateTimeField(blank=True, null=True, db_comment='最后加载时间')

    class Meta:
        managed = False
        db_table = 'analysis_table'

class Charts(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    analysis_sheet_id = models.IntegerField(db_comment='分析表引用外键')
    selected_cases = models.CharField(max_length=255)
    selected_attrs = models.CharField(max_length=255)
    mapping = models.CharField(max_length=255, db_comment='数据映射，存储为JSON')
    axis = models.CharField(max_length=255, db_comment='坐标轴，存储为JSON')
    options = models.CharField(max_length=255, db_comment='常规设置，存储为JSON')

    class Meta:
        managed = False
        db_table = 'charts'



