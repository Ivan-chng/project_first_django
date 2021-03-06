# Generated by Django 2.2.3 on 2021-12-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='教材id')),
                ('book_name', models.CharField(max_length=13, verbose_name='教材名称')),
                ('book_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='教材价格')),
                ('book_pubtdate', models.DateField()),
            ],
            options={
                'ordering': ('book_id',),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='课程id')),
                ('course_name', models.CharField(max_length=13, verbose_name='课程名称')),
                ('course_type', models.CharField(blank=True, max_length=13, null=True, verbose_name='课程类别')),
            ],
            options={
                'ordering': ('course_id',),
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='部门id')),
                ('dept_name', models.CharField(max_length=13, verbose_name='部门名称')),
            ],
            options={
                'ordering': ('dept_id',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='讲师id')),
                ('teacher_name', models.CharField(max_length=13, verbose_name='讲师姓名')),
                ('gender', models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], max_length=8, null=True, verbose_name='讲师性别')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('education', models.CharField(blank=True, choices=[('high school', '高中'), ('bachelor', '本科'), ('postgraduate', '研究生'), ('doctor', '博士')], max_length=12, null=True, verbose_name='学历')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('is_external', models.BooleanField(default=False, verbose_name='是否是外聘')),
            ],
            options={
                'ordering': ('teacher_id',),
            },
        ),
    ]
