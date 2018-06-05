# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-24 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_productpurchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpurchase',
            name='user',
        ),
        migrations.AddField(
            model_name='productpurchase',
            name='order_id',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]