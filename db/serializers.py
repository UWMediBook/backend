from rest_framework import serializers
from db.models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'USER_ID', 'PRIMARY_ID', 'ALLERGY_ID', 'SURGERY_ID', 'VISIT_ID', 'PRESCRIPTION_ID', 'EC_ID', 'F_NAME', 'L_NAME',
        'ADDRESS', 'GENDERS', 'GENDER', 'BIRTHDAY', 'EMAIL', 'PASSWORD', 'HEALTHCARD_NUM', 'CREATED', 'UPDATED')


class emergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = ('EC_ID', 'USER_ID', 'F_NAME', 'L_NAME', 'PHONE_NUM', 'RELATIONSHIP')


class allergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = ('USER_ID', 'ALLERGY_ID', 'ALLERGY')


class prescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('PRESCRIPTION_ID', 'USER_ID', 'PRESCRIPTION')


class pastOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('SURGERY_ID', 'USER_ID', 'OPERATION')


class pastVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('VISIT_ID', 'USER_ID', 'VISIT')


class doctorNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorNote
        fields = ('NOTE_ID', 'USER_ID', 'PRESCRIPTION_ID', 'VISIT_ID', 'SURGERY_ID', 'ALLERGY_ID', 'NOTES')


class primaryDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryDoctor
        fields = ('PRIMARY_ID', 'F_NAME', 'L_NAME')
