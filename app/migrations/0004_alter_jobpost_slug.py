# Generated by Django 4.0.10 on 2024-02-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_jobpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]