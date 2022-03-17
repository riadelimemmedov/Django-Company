# Generated by Django 4.0.2 on 2022-03-03 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('reports', '0002_report_product_report_production_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemReported',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('problem_id', models.CharField(blank=True, max_length=12, unique=True)),
                ('breakdown', models.PositiveIntegerField()),
                ('public', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]