from django.db import models


# Create your models here.

class user(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    doctor_id = models.ForeignKey('primaryDoctor', on_delete=models.CASCADE)
    # ALLERGY_ID = models.ForeignKey('allergy', on_delete=models.CASCADE)
    # SURGERY_ID = models.ForeignKey('pastOperation', on_delete=models.CASCADE)
    # VISIT_ID = models.ForeignKey('pastVisit', on_delete=models.CASCADE)
    # PRESCRIPTION_ID = models.ForeignKey('prescription', on_delete=models.CASCADE)
    # EC_ID = models.ForeignKey('emergencyContact', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=genders)
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    healthcard = models.CharField(max_length=30)
    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)


class emergencyContact(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    relationship = models.CharField(max_length=30)
    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)


class allergy(models.Model):
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    id = models.CharField(max_length=10, primary_key=True)
    allergy = models.TextField(max_length=255)
    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)


class prescription(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    prescription = models.TextField(max_length=255)
    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)


class pastOperation(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    operation = models.TextField(max_length=255)
    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)


class pastVisit(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    visit = models.TextField(max_length=255)
    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)


class doctorNote(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    prescription_id = models.ForeignKey('prescription', on_delete=models.CASCADE)
    visit_id = models.ForeignKey('pastVisit', on_delete=models.CASCADE)
    surgery_id = models.ForeignKey('pastOperation', on_delete=models.CASCADE)
    allergy_id = models.ForeignKey('allergy', on_delete=models.CASCADE)
    note = models.TextField(max_length=255)
    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)


class primaryDoctor(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)
