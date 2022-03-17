# Generated by Django 4.0.2 on 2022-03-09 17:16

from django.db import migrations, models
import reports.models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_alter_problemreported_options_alter_report_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemreported',
            name='problem_id',
            field=models.CharField(blank=True, default=reports.models.random_code, max_length=12, unique=True),
        ),
    ]
