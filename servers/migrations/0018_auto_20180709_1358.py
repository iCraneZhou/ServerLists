# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-09 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0017_auto_20180709_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base_types',
            name='tags',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
