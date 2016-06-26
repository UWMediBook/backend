from django.db import models
import time

# Create your models here.
class Doctor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return dict(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            created_at=time.mktime(self.created_at.timetuple()),
            updated_at=time.mktime(self.updated_at.timetuple())
        )


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name="doctor_users")
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    address = models.CharField(max_length=200, default="")
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'N/A')
    )
    gender = models.CharField(max_length=1, choices=genders, default=genders[2][0])
    birthday = models.DateField()
    email = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="wordpass")
    healthcard = models.CharField(max_length=30, default="123")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return dict(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            address=self.address,
            gender=self.gender,
            birthday=time.mktime(self.birthday.timetuple()),
            email=self.email,
            password=self.password,
            healthcard=self.healthcard,
            doctor=self.doctor.to_dict()
        )

class EmergencyContact(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_contacts")
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30,default="")
    phone_number = models.CharField(max_length=15, default="")
    relationship = models.CharField(max_length=30, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Allergy(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_allergies")
    name = models.CharField(max_length=255, default="")
    severity_choices = (
        ('S', 'Severe'),
        ('M', 'Mild'),
    )
    severity = models.CharField(max_length=1, choices=severity_choices, default=severity_choices[1][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Prescription(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_prescriptions")
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name="doctor_prescriptions")
    name = models.CharField(max_length=255, default="")
    dosage = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Operation(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_operations")
    operation = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Visit(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_visits")
    visit = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DoctorNote(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_notes", null=True)
    prescription = models.ForeignKey('Prescription', on_delete=models.CASCADE, related_name="prescription_notes", null=True)
    visit = models.ForeignKey('Visit', on_delete=models.CASCADE, related_name="visit_notes", null=True)
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE, related_name="operation_notes", null=True)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE, related_name="allergy_notes", null=True)
    note = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



