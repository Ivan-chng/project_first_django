# Generated by Django 2.2.3 on 2021-12-12 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company_training', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='C2B2T',
            fields=[
                ('c2b2t_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='序列id')),
                ('begin_time', models.DateField()),
                ('period', models.IntegerField(verbose_name='学时(h)')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company_training.Book')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_training.Course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_training.Teacher')),
            ],
            options={
                'ordering': ('-c2b2t_id',),
            },
        ),
        migrations.CreateModel(
            name='U2G2M',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(verbose_name='成绩')),
                ('c2b2t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_training.C2B2T')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-c2b2t',),
                'unique_together': {('user', 'c2b2t')},
            },
        ),
    ]
