# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-23 23:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pimpuser_messages', '0004_auto_20171228_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pimpusermessage',
            old_name='message',
            new_name='message_body',
        ),
    ]
