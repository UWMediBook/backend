from rest_framework import serializers
from db.models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class emergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = '__all__'


class allergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = '__all__'


class prescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'


class pastOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


class pastVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class doctorNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorNote
        fields = '__all__'


class primaryDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryDoctor
        fields = '__all__'
