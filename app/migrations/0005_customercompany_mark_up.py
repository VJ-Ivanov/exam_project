# Generated by Django 3.1.3 on 2020-12-03 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_warehouse_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercompany',
            name='mark_up',
            field=models.IntegerField(default=0),
        ),
    ]