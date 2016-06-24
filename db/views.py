from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from db.models import *
from db.serializers import *


def index(request):
    return HttpResponse("<h2>shit's working</h2>")


def users(request):
    users = User.objects.all()
    response = []
    for user in users:
        user_dict = dict(
            id=user.id,
            first_name=user.first_name
        )
        response.append(user_dict)
    return JsonResponse(data=response)


class UserAPIView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        users = [dict(id=user.id, first_name=user.first_name) for user in User.objects.all()]
        return Response(users)


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
