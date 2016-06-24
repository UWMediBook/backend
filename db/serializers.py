from rest_framework import serializers
from db.models import user, prescription, allergy, pastVisit, pastOperation, doctorNote, primaryDoctor, emergencyContact


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = (
        'USER_ID', 'PRIMARY_ID', 'ALLERGY_ID', 'SURGERY_ID', 'VISIT_ID', 'PRESCRIPTION_ID', 'EC_ID', 'F_NAME', 'L_NAME',
        'ADDRESS', 'GENDERS', 'GENDER', 'BIRTHDAY', 'EMAIL', 'PASSWORD', 'HEALTHCARD_NUM', 'CREATED', 'UPDATED')


class emergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = emergencyContact
        fields = ('EC_ID', 'USER_ID', 'F_NAME', 'L_NAME', 'PHONE_NUM', 'RELATIONSHIP')


class allergySerializer(serializers.ModelSerializer):
    class Meta:
        model = allergy
        fields = ('USER_ID', 'ALLERGY_ID', 'ALLERGY')


class prescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = prescription
        fields = ('PRESCRIPTION_ID', 'USER_ID', 'PRESCRIPTION')


class pastOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = pastOperation
        fields = ('SURGERY_ID', 'USER_ID', 'OPERATION')


class pastVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = pastVisit
        fields = ('VISIT_ID', 'USER_ID', 'VISIT')


class doctorNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctorNote
        fields = ('NOTE_ID', 'USER_ID', 'PRESCRIPTION_ID', 'VISIT_ID', 'SURGERY_ID', 'ALLERGY_ID', 'NOTES')


class primaryDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = primaryDoctor
        fields = ('PRIMARY_ID', 'F_NAME', 'L_NAME')
