# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20171019_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beltbuckle',
            name='type',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AlterField(
            model_name='button',
            name='type',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(choices=[('Slider', 'Slider'), ('Button', 'Button'), ('Beltbuckle', 'Beltbuckle'), ('Lace', 'Lace'), ('Waistbelt', 'Waistbelt'), ('Zipper', 'Zipper')], max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='type',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AlterField(
            model_name='waistbelt',
            name='type',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AlterField(
            model_name='zipper',
            name='type',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
    ]