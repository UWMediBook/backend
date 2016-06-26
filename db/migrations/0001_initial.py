# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('severity', models.CharField(choices=[(b'S', b'Severe'), (b'M', b'Mild')], default=b'M', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorNote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('note', models.TextField(default=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('allergy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allergy_notes', to='db.Allergy')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(default=b'', max_length=30)),
                ('last_name', models.CharField(default=b'', max_length=30)),
                ('phone_number', models.CharField(default=b'', max_length=15)),
                ('relationship', models.CharField(default=b'', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('operation', models.TextField(default=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('dosage', models.TextField(default=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_prescriptions', to='db.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(default=b'', max_length=30)),
                ('last_name', models.CharField(default=b'', max_length=30)),
                ('address', models.CharField(default=b'', max_length=200)),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'N', b'N/A')], default=b'N', max_length=1)),
                ('birthday', models.DateField()),
                ('email', models.CharField(default=b'', max_length=255)),
                ('password', models.CharField(default=b'wordpass', max_length=255)),
                ('healthcard', models.CharField(default=b'123', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_users', to='db.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('visit', models.TextField(default=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_visits', to='db.User')),
            ],
        ),
        migrations.AddField(
            model_name='prescription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_prescriptions', to='db.User'),
        ),
        migrations.AddField(
            model_name='operation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_operations', to='db.User'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_contacts', to='db.User'),
        ),
        migrations.AddField(
            model_name='doctornote',
            name='operation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operation_notes', to='db.Operation'),
        ),
        migrations.AddField(
            model_name='doctornote',
            name='prescription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription_notes', to='db.Prescription'),
        ),
        migrations.AddField(
            model_name='doctornote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_notes', to='db.User'),
        ),
        migrations.AddField(
            model_name='doctornote',
            name='visit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visit_notes', to='db.Visit'),
        ),
        migrations.AddField(
            model_name='allergy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_allergies', to='db.User'),
        ),
    ]
