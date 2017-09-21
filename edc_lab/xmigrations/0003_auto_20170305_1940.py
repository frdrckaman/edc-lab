# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_lab', '0002_auto_20170305_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmanifest',
            name='consignee_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Consignee's contact name"),
        ),
        migrations.AddField(
            model_name='historicalmanifest',
            name='shipper_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Shipper's contact name"),
        ),
        migrations.AddField(
            model_name='manifest',
            name='consignee_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Consignee's contact name"),
        ),
        migrations.AddField(
            model_name='manifest',
            name='shipper_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Shipper's contact name"),
        ),
    ]
