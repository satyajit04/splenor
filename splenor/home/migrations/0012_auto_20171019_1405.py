# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20171017_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='beltbuckle',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='button',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lace',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='waistbelt',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='zipper',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(choices=[('Waistbelt', 'Waistbelt'), ('Zipper', 'Zipper'), ('Slider', 'Slider'), ('Lace', 'Lace'), ('Button', 'Button'), ('Beltbuckle', 'Beltbuckle')], max_length=50),
        ),
    ]