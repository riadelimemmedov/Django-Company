# Generated by Django 4.0.2 on 2022-03-02 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('profiles', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('products', models.ManyToManyField(to='products.Product')),
                ('team_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]