# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(choices=[('Beltbuckle', 'Beltbuckle'), ('Button', 'Button'), ('Lace', 'Lace'), ('Slider', 'Slider'), ('Waistbelt', 'Waistbelt'), ('Zipper', 'Zipper')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='beltbuckle',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AddField(
            model_name='button',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AddField(
            model_name='lace',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AddField(
            model_name='slider',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AddField(
            model_name='waistbelt',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AddField(
            model_name='zipper',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
    ]
