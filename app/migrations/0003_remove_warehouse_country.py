# Generated by Django 3.1.3 on 2020-12-01 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201130_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='country',
        ),
    ]
