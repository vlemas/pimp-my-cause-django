# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-10-20 21:52
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_auto_20171017_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='pimpuser',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326),
            preserve_default=False,
        ),
    ]