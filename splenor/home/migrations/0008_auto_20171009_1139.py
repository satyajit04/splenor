# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-09 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20171009_1130'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(choices=[('Waistbelt', 'Waistbelt'), ('Lace', 'Lace'), ('Slider', 'Slider'), ('Button', 'Button'), ('Beltbuckle', 'Beltbuckle'), ('Zipper', 'Zipper')], max_length=50),
        ),
    ]