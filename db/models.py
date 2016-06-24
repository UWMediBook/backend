from django.db import models
from django.utils.timezone import now


# Create your models here.
class PrimaryDoctor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True, default=now())
    updated_at = models.DateField(auto_now=True, default=now())


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    doctor = models.ForeignKey('PrimaryDoctor', on_delete=models.CASCADE, related_name="doctor_users")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'N/A')
    )
    gender = models.CharField(max_length=1, choices=genders, default=genders[2])
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    healthcard = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True, default=now())
    updated_at = models.DateField(auto_now=True, default=now())


class EmergencyContact(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_contacts")
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=15, default="")
    relationship = models.CharField(max_length=30, default="")
    created_at = models.DateField(auto_now_add=True, default=now())
    updated_at = models.DateField(auto_now=True, default=now())


class Allergy(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_allergies")
    name = models.CharField(max_length=255, default="")
    severity_choices = (
        ('S', 'Severe'),
        ('M', 'Mild'),
    )
    severity = models.CharField(max_length=1, choices=severity_choices, default=severity_choices[1])
    created_at = models.DateField(auto_now_add=True, default=now())
    updated_at = models.DateField(auto_now=True, default=now())


class Prescription(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_prescriptions")
    doctor = models.ForeignKey('PrimaryDoctor', on_delete=models.CASCADE, related_name="doctor_prescriptions")
    name = models.CharField(max_length=255, default="")
    dosage = models.TextField(default="")
    created_at = models.DateField(auto_now_add=True, default=now())
    updated_at = models.DateField(auto_now=True, default=now())


class Operation(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_operations")
    operation = models.TextField(default="")
    created_at = models.DateField(auto_now_add=True, default=now())
    updated_at = models.DateField(auto_now=True, default=now())


class Visit(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_visits")
    visit = models.TextField(default="")
    created_at = models.DateField(auto_now_add=True, default=now())
    updated_at = models.DateField(auto_now=True, default=now())


class DoctorNote(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_notes", null=True)
    prescription = models.ForeignKey('Prescription', on_delete=models.CASCADE, related_name="prescription_notes",
                                     null=True)
    visit = models.ForeignKey('Visit', on_delete=models.CASCADE, related_name="visit_notes", null=True)
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE, related_name="operation_notes", null=True)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE, related_name="allergy_notes", null=True)
    note = models.TextField(default="")
    created_at = models.DateField(auto_now_add=True, default=now())
    updated_at = models.DateField(auto_now=True, default=now())
