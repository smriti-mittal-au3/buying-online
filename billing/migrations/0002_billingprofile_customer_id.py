# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingprofile',
            name='customer_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
