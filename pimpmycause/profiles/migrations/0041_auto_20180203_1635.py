# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-03 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0040_auto_20180203_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pimpuser',
            name='city',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
