# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 03:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20160719_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_doctor',
        ),
    ]