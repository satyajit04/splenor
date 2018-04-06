# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20171022_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='beltbuckle',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='button',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='lace',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='waistbelt',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='zipper',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='zipper',
            name='style',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Vislon', 'Vislon'), ('Coil', 'Coil'), ('Invisible', 'Invisible')], max_length=21),
        ),
        migrations.AlterField(
            model_name='button',
            name='style',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Two Hole', 'Two Hole'), ('Four Hole', 'Four Hole'), ('Press', 'Press'), ('Shank', 'Shank'), ('Hook and Eye', 'Hook and Eye'), ('Coat', 'Coat'), ('Shirt', 'Shirt'), ('Cardigan', 'Cardigan'), ('Toggle', 'Toggle'), ('Decorative', 'Decorative')], max_length=81),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(choices=[('Waistbelt', 'Waistbelt'), ('Slider', 'Slider'), ('Button', 'Button'), ('Zipper', 'Zipper'), ('Beltbuckle', 'Beltbuckle'), ('Lace', 'Lace')], max_length=50),
        ),
        migrations.AlterField(
            model_name='zipper',
            name='category',
            field=models.CharField(choices=[('Metal', 'Metal'), ('Plastic', 'Plastic'), ('Nylon', 'Nylon')], max_length=100),
        ),
    ]