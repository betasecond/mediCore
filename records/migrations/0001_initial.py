# Generated by Django 5.1.6 on 2025-02-09 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('case_id', models.IntegerField(db_comment='病历外键引用')),
                ('table_name', models.CharField(max_length=255)),
                ('data_template_id', models.IntegerField(db_comment='引用数�\x8d�模�\x9d�外键')),
            ],
            options={
                'db_table': 'data_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentChart',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('document_id', models.IntegerField()),
                ('chart_id', models.IntegerField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
            ],
            options={
                'db_table': 'document_chart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('properties', models.CharField(db_comment='属性，�\xad�JSON', max_length=255)),
            ],
            options={
                'db_table': 'documents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExaminationImages',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('examination_sheet_id', models.IntegerField(db_comment='检查表外键引用')),
                ('url', models.CharField(max_length=255)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'examination_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExaminationSheet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data_table_id', models.IntegerField(db_comment='数�\x8d�表外键引用')),
                ('case_id', models.IntegerField(blank=True, db_comment='病历冗余�\xad�储', null=True)),
                ('name', models.CharField(max_length=255)),
                ('name_code', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('category_code', models.CharField(max_length=255)),
                ('diagnosis', models.CharField(db_comment='诊�\xad', max_length=255)),
                ('description', models.CharField(blank=True, db_comment='检查�\x8f\x8f述', max_length=255, null=True)),
                ('exam_date', models.DateTimeField()),
                ('inspector', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'examination_sheet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('document_id', models.IntegerField(db_comment='文档引用')),
                ('url', models.CharField(max_length=255)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('is_stroke', models.IntegerField()),
                ('stroke_weight', models.FloatField(db_comment='�\x8f\x8f边粗细')),
                ('stroke_color', models.CharField(db_comment='�\x8f\x8f边颜色', max_length=255)),
            ],
            options={
                'db_table': 'image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('document_id', models.IntegerField(db_comment='文档引用')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('is_fill', models.IntegerField()),
                ('fill_color', models.CharField(db_comment='填充颜色', max_length=255)),
                ('is_stroke', models.IntegerField()),
                ('stroke_color', models.CharField(db_comment='�\x8f\x8f边颜色', max_length=255)),
                ('path', models.CharField(db_comment='点集，�\xad�JSON', max_length=255)),
            ],
            options={
                'db_table': 'shape',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestingSheet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data_table_id', models.IntegerField(db_comment='数�\x8d�表外键引用')),
                ('case_id', models.IntegerField(blank=True, db_comment='病历冗余�\xad�储', null=True)),
                ('name', models.CharField(max_length=255)),
                ('name_code', models.CharField(max_length=255)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_short', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('category_code', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('type_code', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('test_date', models.DateTimeField()),
                ('inspector', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'testing_sheet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('document_id', models.IntegerField(db_comment='文档引用')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('family', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('underline', models.IntegerField()),
                ('slope', models.IntegerField()),
            ],
            options={
                'db_table': 'text',
                'managed': False,
            },
        ),
    ]
