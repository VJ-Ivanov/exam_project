# Generated by Django 3.1.3 on 2020-12-04 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201203_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercompany',
            name='company_logo',
            field=models.URLField(default='https://i.pinimg.com/236x/fc/7e/ce/fc7ece8e8ee1f5db97577a4622f33975--photo-icon-sad.jpg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transportcompany',
            name='company_logo',
            field=models.URLField(default='https://i.pinimg.com/236x/fc/7e/ce/fc7ece8e8ee1f5db97577a4622f33975--photo-icon-sad.jpg'),
            preserve_default=False,
        ),
    ]
