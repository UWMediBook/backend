from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from db.models import *
from db.serializers import *
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    return HttpResponse("<h2>shit's working</h2>")


def users(request):
    query = User.objects.all()
    request_params = request.GET
    email = request_params.get("email", None)
    if email:
        query = query.filter(email=email)
    serialized_json = serializers.serialize("json", query)
    return HttpResponse(serialized_json, content_type="application/json")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class DoctorNoteViewSet(viewsets.ModelViewSet):
    queryset = DoctorNote.objects.all()
    serializer_class = DoctorNoteSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
