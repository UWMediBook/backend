from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from db.models import *
from db.serializers import *
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.http import require_GET, require_POST
from datetime import datetime
from datetime import date
import time
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return HttpResponse("<h2>shit's working</h2>")


@csrf_exempt
def users(request):
    if request.method == "GET":
        query = User.objects.all()
        request_params = request.GET

        email = request_params.get("email", None)
        if email:
            query = query.filter(email=email)

        serialized_json = serializers.serialize("json", query)

        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        first_name = request_params.get("first_name", "")
        last_name = request_params.get("last_name", "")
        address = request_params.get("address", "")
        gender = request_params.get("gender", "N")
        # birthday = request_params.get("birthday", time.time())
        birthday = datetime.fromtimestamp(time.time())
        email = request_params.get("email", "")
        password = request_params.get("last_name", "wordpass")
        healthcard = request_params.get("healthcard", "")
        doctor_id = request_params.get("doctor_id", None)
        if not doctor_id:
            raise Exception("Invalid Doctor ID")
        doctor = Doctor.objects.get(id=doctor_id)
        if not doctor:
            raise Exception("Invalid Doctor")

        user = User(first_name=first_name, last_name=last_name, address=address, gender=gender, birthday=birthday,
                    email=email, password=password, healthcard=healthcard, doctor=doctor)
        user.save()

        return HttpResponse(json.dumps(user.to_dict()), content_type="application/json")
    elif request.method == "PUT":
        # TODO: implement this
        query = User.objects.all()
        serialized_json = serializers.serialize("json", query)

        return HttpResponse(serialized_json, content_type="application/json")


def allergies(request):
    if request.method == "GET":
        query = Allergy.objects.all()

        serialized_json = serializers.serialize("json", query)

        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "POST":
        request_params = request.POST
        user_id = request_params.get("user_id", None)
        if not user_id:
            raise Exception("Invalid user id")

        user = User.objects.get(user_id)
        if not user:
            raise Exception("Invalid user")

        name = request_params.get("name", "")
        severity = request_params.get("severity", "M")

        allergy = Allergy(user=user, name=name, severity=severity)
        allergy.save()

        return HttpResponse(DjangoJSONEncoder().default(allergy), content_type="application/json")
    elif request.method == "PUT":
        # TODO: implement this
        query = User.objects.all()
        serialized_json = serializers.serialize("json", query)

        return HttpResponse(serialized_json, content_type="application/json")


@csrf_exempt
def doctors(request):
    if request.method == "GET":
        query = Doctor.objects.all()

        serialized_json = serializers.serialize("json", query)

        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)

        first_name = request_params.get("first_name", "")
        last_name = request_params.get("last_name", "")

        doctor = Doctor(first_name=first_name, last_name=last_name)
        doctor.save()

        response = dict(
            id=doctor.id,
            first_name=doctor.first_name,
            last_name=doctor.last_name,
            created_at=time.mktime(doctor.created_at.timetuple()),
            updated_at=time.mktime(doctor.updated_at.timetuple()),
        )

        return HttpResponse(json.dumps(response), content_type="application/json")
    elif request.method == "PUT":
        # TODO: implement this
        query = User.objects.all()
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
