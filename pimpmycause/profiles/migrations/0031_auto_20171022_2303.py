# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 23:03
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0030_auto_20171022_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pimpuser',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
