# Generated by Django 2.1.7 on 2019-03-05 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_name', models.CharField(max_length=255, verbose_name='名称')),
                ('sp_type', models.CharField(choices=[('percent', '折扣百分比'), ('decrease', '减免数额'), ('free', '免费')], max_length=255, verbose_name='类型')),
                ('sp_value', models.FloatField(verbose_name='面额')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('start_time', models.DateTimeField(verbose_name='起始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '课程体系活动',
                'verbose_name_plural': '课程体系活动',
                'db_table': 'code_activity_sp',
                'ordering': ['-id'],
            },
        ),
    ]
