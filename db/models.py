from django.db import models


# Create your models here.
class PrimaryDoctor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    doctor = models.ForeignKey('PrimaryDoctor', on_delete=models.CASCADE, related_name="users")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'N/A')
    )
    gender = models.CharField(max_length=1, choices=genders)
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    healthcard = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class EmergencyContact(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="emergency_contacts")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    relationship = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Allergy(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="emergency_contacts")
    name = models.CharField(max_length=255)
    severity_choices = (
        ('S', 'Severe'),
        ('M', 'Mild'),
    )
    severity = models.CharField(max_length=1, choices=severity_choices)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Prescription(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="emergency_contacts")
    doctor = models.ForeignKey('PrimaryDoctor', on_delete=models.CASCADE, related_name="prescriptions")
    name = models.CharField(max_length=255)
    dosage = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



class Operation(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="emergency_contacts")
    operation = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Visit(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="emergency_contacts")
    visit = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class DoctorNote(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="emergency_contacts")
    prescription = models.ForeignKey('Prescription', on_delete=models.CASCADE, related_name="notes")
    visit = models.ForeignKey('Visit', on_delete=models.CASCADE, related_name="notes")
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE, related_name="notes")
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE, related_name="notes")
    note = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



