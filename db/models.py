from django.db import models

# Create your models here.

class main(models.Model):
	USER_ID = models.CharField(max_length=10, primary_key=True)
	PRIMARY_ID = models.ForeignKey('primaryDoctor',on_delete=models.CASCADE)
	ALLERGY_ID = models.ForeignKey('allergy',on_delete=models.CASCADE)
	SURGERY_ID = models.ForeignKey('pastOperation',on_delete=models.CASCADE)
	VISIT_ID = models.ForeignKey('pastVisit',on_delete=models.CASCADE)
	PRESCRIPTION_ID = models.ForeignKey('prescription',on_delete=models.CASCADE)
	EC_ID = models.ForeignKey('emergencyContact',on_delete=models.CASCADE)
	F_NAME = models.CharField(max_length=20)
	L_NAME = models.CharField(max_length=20)
	ADDRESS = models.CharField(max_length=200)
	GENDERS = (
		('M', 'Male'),
		('F', 'Female'),
		)
	GENDER = models.CharField(max_length=1, choices=GENDERS)
	BIRTHDAY = models.DateField()
	EMAIL = models.CharField(max_length=30)
	PASSWORD = models.CharField(max_length=255)
	HEALTHCARD_NUM = models.CharField(max_length=10)
	CREATED = models.DateField()
	UPDATED = models.DateField()

class emergencyContact(models.Model):
	EC_ID = models.CharField(max_length=10, primary_key = True)
	USER_ID = models.ForeignKey('main', on_delete=models.CASCADE)
	F_NAME = models.CharField(max_length=20)
	L_NAME = models.CharField(max_length=20)
	PHONE_NUM = models.CharField(max_length=10)
	RELATIONSHIP = models.CharField(max_length=15)

class allergy(models.Model):
	USER_ID = models.ForeignKey('main', on_delete=models.CASCADE)
	ALLERGY_ID = models.CharField(max_length=10, primary_key = True)
	ALLERGY = models.TextField(max_length=255)

class prescription(models.Model):
	PRESCRIPTION_ID = models.CharField(max_length=10, primary_key = True)
	USER_ID = models.ForeignKey('main', on_delete=models.CASCADE)
	PRESCRIPTION = models.TextField(max_length=255)

class pastOperation(models.Model):
	SURGERY_ID = models.CharField(max_length=10, primary_key = True)
	USER_ID = models.ForeignKey('main', on_delete=models.CASCADE)
	OPERATION = models.TextField(max_length=255)

class pastVisit(models.Model):
	VISIT_ID = models.CharField(max_length=10, primary_key = True)
	USER_ID = models.ForeignKey('main', on_delete=models.CASCADE)
	VISIT = models.TextField(max_length=255)

class doctorNote(models.Model):
	NOTE_ID = models.CharField(max_length=10, primary_key = True)
	USER_ID = models.ForeignKey('main', on_delete=models.CASCADE)
	PRESCRIPTION_ID = models.ForeignKey('prescription', on_delete=models.CASCADE)
	VISIT_ID = models.ForeignKey('pastVisit', on_delete=models.CASCADE)
	SURGERY_ID = models.ForeignKey('pastOperation', on_delete=models.CASCADE)
	ALLERGY_ID = models.ForeignKey('allergy', on_delete=models.CASCADE)
	NOTES = models.TextField(max_length=255)

class primaryDoctor(models.Model):
	PRIMARY_ID = models.CharField(max_length=10, primary_key = True)
	F_NAME = models.CharField(max_length=20)
	L_NAME = models.CharField(max_length=20)
