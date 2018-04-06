# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-09 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170809_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(choices=[('Lace', 'Lace'), ('Beltbuckle', 'Beltbuckle'), ('Waistbelt', 'Waistbelt'), ('Button', 'Button'), ('Zipper', 'Zipper'), ('Slider', 'Slider')], max_length=50),
        ),
    ]
