# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctornote',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_notes', to='db.Doctor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
    ]