# Generated by Django 3.1.3 on 2020-12-13 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20201212_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transportrequest',
            name='published',
        ),
        migrations.RemoveField(
            model_name='transportrequest',
            name='quote_completed',
        ),
    ]