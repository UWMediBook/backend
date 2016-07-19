# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20160717_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(default=b'', max_length=30)),
                ('last_name', models.CharField(default=b'', max_length=30)),
                ('phone_number', models.CharField(default=b'', max_length=15)),
                ('address', models.CharField(default=b'', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default=b'wordpass', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_users', to='db.Doctor'),
        ),
        migrations.AddField(
            model_name='physician',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_physicians', to='db.User'),
        ),
    ]
