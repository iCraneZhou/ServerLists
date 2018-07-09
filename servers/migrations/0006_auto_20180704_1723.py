# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-04 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0005_auto_20180704_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base_types',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='base_types',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='configuration_lists',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='configuration_lists',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='configurations',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='configurations',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hardware_accessories',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='hardware_accessories',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]