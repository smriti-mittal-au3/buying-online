# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-23 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180423_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
