from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from db.models import main,allergy,pastVisit,pastOperation,doctorNote,prescription,emergencyContact,primaryDoctor
from db.serializers import mainSerializer, pastVisitSerializer,pastOperationSerializer,doctorNoteSerializer,prescriptionSerializer,emergencyContactSerializer,primaryDoctorSerializer,allergySerializer

def index(request):
	return HttpResponse("<h2>shit's working</h2>")

class mainViewSet(viewsets.ModelViewSet):
	queryset = main.objects.all()
	serializer_class = mainSerializer

class allergyViewSet(viewsets.ModelViewSet):
	queryset = allergy.objects.all()
	serializer_class = allergySerializer

class pastVisitViewSet(viewsets.ModelViewSet):
	queryset = pastVisit.objects.all()
	serializer_class = pastVisitSerializer

class pastOperationViewSet(viewsets.ModelViewSet):
	queryset = pastOperation.objects.all()
	serializer_class = pastOperationSerializer
	
class doctorNoteViewSet(viewsets.ModelViewSet):
	queryset = doctorNote.objects.all()
	serializer_class = doctorNoteSerializer
	
class prescriptionViewSet(viewsets.ModelViewSet):
	queryset = prescription.objects.all()
	serializer_class = prescriptionSerializer
	
class emergencyContactViewSet(viewsets.ModelViewSet):
	queryset = emergencyContact.objects.all()
	serializer_class = emergencyContactSerializer
	
class primaryDoctorViewSet(viewsets.ModelViewSet):
	queryset = primaryDoctor.objects.all()
	serializer_class = primaryDoctorSerializer
	
