from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from db.models import *
from db.serializers import *


def index(request):
    return HttpResponse("<h2>shit's working</h2>")


class mainViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer


class allergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = allergySerializer


class pastVisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = pastVisitSerializer


class pastOperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = pastOperationSerializer


class doctorNoteViewSet(viewsets.ModelViewSet):
    queryset = DoctorNote.objects.all()
    serializer_class = doctorNoteSerializer


class prescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = prescriptionSerializer


class emergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = emergencyContactSerializer


class primaryDoctorViewSet(viewsets.ModelViewSet):
    queryset = PrimaryDoctor.objects.all()
    serializer_class = primaryDoctorSerializer
