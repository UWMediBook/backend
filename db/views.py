from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseNotAllowed
from rest_framework import viewsets
from db.serializers import *
from django.core import serializers
from datetime import datetime
import time
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import BCryptPasswordHasher
import random

@csrf_exempt
def authenticate(request):
    if request.method == "POST":
        request_params = json.loads(request.body)
        email = request_params.get("email", None)
        password = request_params.get("password", None)
        if not email or not password:
            return HttpResponseBadRequest("Missing email or password")

        user = User.objects.get(email=email)
        if not user:
            return HttpResponseNotFound("User does not exist")

        if BCryptPasswordHasher().verify(password, user.password):
            response = dict(
                token=random.getrandbits(64),
                is_doctor=int(user.is_doctor)
            )
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            return HttpResponseNotAllowed("Invalid email/password")


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
    elif request.method == "PUT":
        request_params = json.loads(request.body)
        first_name = request_params.get("first_name", "")
        last_name = request_params.get("last_name", "")
        address = request_params.get("address", "")
        gender = request_params.get("gender", "N")
        birthday = request_params.get("birthday", time.time())
        birthday = datetime.fromtimestamp(birthday)
        email = request_params.get("email", "")
        password = request_params.get("password", "wordpass")
        healthcard = request_params.get("healthcard", "")
        doctor_id = request_params.get("doctor_id", None)
        if not doctor_id:
            return HttpResponseBadRequest("Empty Doctor ID")
        doctor = Doctor.objects.get(id=doctor_id)
        if not doctor:
            return HttpResponseNotFound("Unable to find doctor")

        user = User(first_name=first_name, last_name=last_name, address=address, gender=gender, birthday=birthday,
                    email=email,
                    password=BCryptPasswordHasher().encode(password=password, salt=BCryptPasswordHasher().salt()),
                    healthcard=healthcard, doctor=doctor)
        user.save()

        return HttpResponse(json.dumps(user.to_dict()), content_type="application/json")


@csrf_exempt
def users_by_id(request, user_id):
    if request.method == "GET":
        user = User.objects.get(id=user_id)
        if not user:
            return HttpResponseNotFound("User not found")
        return HttpResponse(json.dumps(user.to_dict()), content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        user = User.objects.get(id=user_id)
        if not user:
            return HttpResponseNotFound("Unable to find doctor")
        first_name = request_params.get("first_name", None)
        last_name = request_params.get("last_name", None)
        address = request_params.get("address", None)
        gender = request_params.get("gender", None)
        birthday = request_params.get("birthday", None)
        birthday = datetime.fromtimestamp(birthday)
        email = request_params.get("email", None)
        password = request_params.get("password", None)
        healthcard = request_params.get("healthcard", None)
        doctor_id = request_params.get("doctor_id", None)
        doctor = None
        if doctor_id:
            doctor = Doctor.objects.get(id=doctor_id)
            if not doctor:
                return HttpResponseNotFound("Unable to find doctor")
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if address:
            user.address = address
        if gender:
            user.gender = gender
        if birthday:
            user.birthday = birthday
        if email:
            user.email = email
        if password:
            user.password = BCryptPasswordHasher().encode(password=password, salt=BCryptPasswordHasher().salt())
        if healthcard:
            user.healthcard = healthcard
        if doctor:
            user.doctor = doctor

        user.save()

        return HttpResponse(json.dumps(user.to_dict()), content_type="application/json")


@csrf_exempt
def users_by_email(request, email):
    if request.method == "GET":
        user = User.objects.get(email=email)
        if not user:
            return HttpResponseNotFound("User not found")
        return HttpResponse(json.dumps(user.to_dict()), content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        user = User.objects.get(email=email)
        if not user:
            return HttpResponseNotFound("Unable to find doctor")
        first_name = request_params.get("first_name", None)
        last_name = request_params.get("last_name", None)
        address = request_params.get("address", None)
        gender = request_params.get("gender", None)
        birthday = request_params.get("birthday", None)
        email = request_params.get("email", None)
        password = request_params.get("password", None)
        healthcard = request_params.get("healthcard", None)
        doctor_id = request_params.get("doctor_id", None)
        doctor = None
        if doctor_id:
            doctor = Doctor.objects.get(id=doctor_id)
            if not doctor:
                return HttpResponseNotFound("Unable to find doctor")
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if address:
            user.address = address
        if gender:
            user.gender = gender
        if birthday:
            user.birthday = birthday
        if email:
            user.email = email
        if password:
            user.password = password
        if healthcard:
            user.healthcard = healthcard
        if doctor:
            user.doctor = doctor

        user.save()

        return HttpResponse(json.dumps(user.to_dict()), content_type="application/json")


@csrf_exempt
def doctors(request):
    if request.method == "GET":
        query = Doctor.objects.all()
        serialized_json = serializers.serialize("json", query)
        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "PUT":
        request_params = json.loads(request.body)

        first_name = request_params.get("first_name", "")
        last_name = request_params.get("last_name", "")

        doctor = Doctor(first_name=first_name, last_name=last_name)
        doctor.save()

        return HttpResponse(json.dumps(doctor.to_dict()), content_type="application/json")


@csrf_exempt
def doctors_by_id(request, doctor_id):
    if request.method == "GET":
        doctor = Doctor.objects.get(id=doctor_id)
        return HttpResponse(json.dumps(doctor.to_dict()), content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        doctor = Doctor.objects.get(id=doctor_id)
        if not doctor:
            return HttpResponseNotFound("Unable to find doctor")
        first_name = request_params.get("first_name", None)
        last_name = request_params.get("last_name", None)
        if first_name:
            doctor.first_name = first_name
        if last_name:
            doctor.last_name = last_name
        doctor.save()
        return HttpResponse(json.dumps(doctor.to_dict()), content_type="application/json")


@csrf_exempt
def emergency_contacts(request):
    if request.method == "GET":
        query = EmergencyContact.objects.all()
        serialized_json = serializers.serialize("json", query)

        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "PUT":
        request_params = json.loads(request.body)

        user_id = request_params.get("user_id", None)
        if not user_id:
            raise Exception("Invalid User ID")

        user = User.objects.get(id=user_id)

        if not user:
            raise Exception("Invalid User")

        first_name = request_params.get("first_name", "")
        last_name = request_params.get("last_name", "")
        phone_number = request_params.get("phone_number", "")
        relationship = request_params.get("relationship", "Unspecified")

        contact = EmergencyContact(user=user, first_name=first_name, last_name=last_name, phone_number=phone_number,
                                   relationship=relationship)
        contact.save()

        return HttpResponse(json.dumps(contact.to_dict()), content_type="application/json")


@csrf_exempt
def emergency_contacts_by_id(request, contact_id):
    if request.method == "GET":
        emergency_contact = EmergencyContact.objects.get(id=contact_id)
        if not emergency_contact:
            return HttpResponseNotFound("Emergency Contact Not Found")
        return HttpResponse(json.dumps(emergency_contact.to_dict()), content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        contact = EmergencyContact.objects.get(id=contact_id)
        if not contact:
            return HttpResponseNotFound("Emergency Contact Not Found")

        first_name = request_params.get("first_name", None)
        last_name = request_params.get("last_name", None)
        phone_number = request_params.get("phone_number", None)
        relationship = request_params.get("relationship", None)

        if first_name:
            contact.first_name = first_name
        if last_name:
            contact.last_name = last_name
        if phone_number:
            contact.phone_number = phone_number
        if relationship:
            contact.relationship = relationship

        contact.save()

        return HttpResponse(json.dumps(contact.to_dict()), content_type="application/json")

@csrf_exempt
def emergency_contacts_by_user_id(request, user_id):
    if request.method == "GET":
        response = list()
        ecs = EmergencyContact.objects.all()
        for ec in ecs:
            if ec.user.id == int(user_id):
                response.append(ec.to_dict())
        return HttpResponse(json.dumps(response), content_type="application/json")


@csrf_exempt
def allergies(request):
    if request.method == "GET":
        query = Allergy.objects.all()
        serialized_json = serializers.serialize("json", query)
        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "PUT":
        request_params = json.loads(request.body)
        user_id = request_params.get("user_id", None)
        if not user_id:
            raise Exception("Invalid user id")

        user = User.objects.get(id=user_id)
        if not user:
            raise Exception("Invalid user")

        name = request_params.get("name", "")
        severity = request_params.get("severity", "M")

        allergy = Allergy(user=user, name=name, severity=severity)
        allergy.save()

        return HttpResponse(json.dumps(allergy.to_dict()), content_type="application/json")


@csrf_exempt
def allergies_by_id(request, allergy_id):
    if request.method == "GET":
        allergy = Allergy.objects.get(id=allergy_id)
        return HttpResponse(json.dumps(allergy), content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        allergy = Allergy.objects.get(id=allergy_id)
        if not allergy:
            return HttpResponseNotFound("Unable to find allergy")

        name = request_params.get("name", None)
        severity = request_params.get("severity", None)

        if name:
            allergy.name = name
        if severity:
            allergy.severity = severity

        allergy.save()
        return HttpResponse(json.dumps(allergy.to_dict()), content_type="application/json")


@csrf_exempt
def allergies_by_user_id(request, user_id):
    if request.method == "GET":
        response = list()
        alls = Allergy.objects.all()
        for a in alls:
            if a.user.id == int(user_id):
                response.append(a.to_dict())
        return HttpResponse(json.dumps(response), content_type="application/json")



@csrf_exempt
def prescriptions(request):
    if request.method == "GET":
        query = Prescription.objects.all()
        serialized_json = serializers.serialize("json", query)
        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "PUT":
        request_params = json.loads(request.body)
        user_id = request_params.get("user_id", None)
        if not user_id:
            raise Exception("Invalid User ID")
        user = User.objects.get(id=user_id)
        if not user:
            raise Exception("Invalid User")

        doctor_id = request_params.get("doctor_id", None)
        if not doctor_id:
            raise Exception("Invalid Doctor ID")
        doctor = Doctor.objects.get(id=doctor_id)
        if not doctor:
            raise Exception("Invalid Doctor")

        name = request_params.get("name", "")
        dosage = request_params.get("dosage", "")

        prescription = Prescription(user=user, doctor=doctor, name=name, dosage=dosage)
        prescription.save()

        return HttpResponse(json.dumps(prescription.to_dict()), content_type="application/json")


@csrf_exempt
def prescriptions_by_id(request, prescription_id):
    if request.method == "GET":
        prescription = Prescription.objects.get(id=prescription_id)
        return HttpResponse(json.dumps(prescription.to_dict()), content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        prescription = Prescription.objects.get(id=prescription_id)
        if not prescription:
            return HttpResponseNotFound("Prescription not found")

        name = request_params.get("name", None)
        dosage = request_params.get("dosage", None)
        if name:
            prescription.name = name
        if dosage:
            prescription.dosage = dosage
        prescription.save()

        return HttpResponse(json.dumps(prescription.to_dict()), content_type="application/json")


@csrf_exempt
def prescriptions_by_user_id(request, user_id):
    if request.method == "GET":
        response = list()
        prescrips = Prescription.objects.all()
        for p in prescrips:
            if p.user.id == int(user_id):
                response.append(p.to_dict())
        return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def operations(request):
    if request.method == "GET":
        query = Operation.objects.all()
        serialized_json = serializers.serialize("json", query)
        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "PUT":
        request_params = json.loads(request.body)
        user_id = request_params.get("user_id", None)
        if not user_id:
            raise Exception("Invalid User ID")
        user = User.objects.get(id=user_id)
        if not user:
            raise Exception("Invalid User")

        operation_details = request_params.get("operation", "")

        operation = Operation(user=user, operation=operation_details)
        operation.save()

        return HttpResponse(json.dumps(operation.to_dict()), content_type="application/json")


@csrf_exempt
def operations_by_id(request, operation_id):
    if request.method == "GET":
        operation = Operation.objects.get(id=operation_id)
        if not operation:
            return HttpResponseNotFound("Unable to find operation")
        return HttpResponse(json.dumps(operation.to_dict()), content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        operation = Operation.objects.get(id=operation_id)
        if not operation:
            return HttpResponseNotFound("Unable to find operation")

        operation_details = request_params.get("operation", None)
        if operation_details:
            operation.operation = operation_details

        operation.save()

        return HttpResponse(json.dumps(operation.to_dict()), content_type="application/json")


@csrf_exempt
def operations_by_user_id(request, user_id):
    if request.method == "GET":
        response = list()
        ops = Operation.objects.all()
        for o in ops:
            if o.user.id == int(user_id):
                response.append(o.to_dict())
        return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def visits(request):
    if request.method == "GET":
        query = Visit.objects.all()
        serialized_json = serializers.serialize("json", query)
        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "PUT":
        request_params = json.loads(request.body)
        user_id = request_params.get("user_id", None)
        if not user_id:
            raise Exception("Invalid User ID")
        user = User.objects.get(id=user_id)
        if not user:
            raise Exception("Invalid User")

        visit_details = request_params.get("visit", "")

        visit = Visit(user=user, visit=visit_details)
        visit.save()

        return HttpResponse(json.dumps(visit.to_dict()), content_type="application/json")


@csrf_exempt
def visits_by_id(request, visit_id):
    if request.method == "GET":
        visit = Visit.objects.get(id=visit_id)
        if not visit:
            return HttpResponseNotFound("Unable to find visit")
        return HttpResponse(json.dumps(visit.to_dict()), content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        visit = Visit.objects.get(id=visit_id)
        if not visit:
            return HttpResponseNotFound("Unable to find visit")

        visit_details = request_params.get("visit", None)
        if visit_details:
            visit.visit = visit_details
        visit.save()

        return HttpResponse(json.dumps(visit.to_dict()), content_type="application/json")


@csrf_exempt
def visits_by_user_id(request, user_id):
    if request.method == "GET":
        response = list()
        vis = Visit.objects.all()
        for v in vis:
            if v.user.id == int(user_id):
                response.append(v.to_dict())
        return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def doctor_notes(request):
    if request.method == "GET":
        query = DoctorNote.objects.all()
        serialized_json = serializers.serialize("json", query)
        return HttpResponse(serialized_json, content_type="application/json")
    elif request.method == "POST":
        request_params = json.loads(request.body)
        note_id = request_params.get("note_id", None)

        if not note_id:
            raise Exception()
        doctor_note = DoctorNote.objects.get(id=note_id)

        if not doctor_note:
            raise Exception()

        notes = request_params.get("notes", None)
        if notes:
            doctor_note.note = notes
        doctor_note.save()

        return HttpResponse(json.dumps(doctor_note.to_dict()), content_type="application/json")
    elif request.method == "PUT":
        request_params = json.loads(request.body)
        doctor_id = request_params.get("doctor_id", None)
        if not doctor_id:
            raise Exception("Empty doctor ID")
        doctor = Doctor.objects.get(id=doctor_id)
        if not doctor:
            raise Exception("Unable to find doctor")
        user = None
        prescription = None
        visit = None
        operation = None
        allergy = None
        user_id = request_params.get("user_id", None)
        prescription_id = request_params.get("prescription_id", None)
        visit_id = request_params.get("visit_id", None)
        operation_id = request_params.get("operation_id", None)
        allergy_id = request_params.get("allergy_id", None)
        if user_id:
            user = User.objects.get(id=user_id)
            if not user:
                raise Exception("Invalid User")
        elif prescription_id:
            prescription = Prescription.objects.get(id=prescription_id)
            if not prescription:
                raise Exception("Invalid Prescription")
        elif visit_id:
            visit = Visit.objects.get(id=visit_id)
            if not visit:
                raise Exception("Invalid Visit")
        elif operation_id:
            operation = Operation.objects.get(id=operation_id)
            if not operation:
                raise Exception("Invalid Operation")
        elif allergy_id:
            allergy = Allergy.objects.get(id=allergy_id)
            if not allergy:
                raise Exception("Invalid Allergy")
        else:
            raise Exception("No object ID supplied")

        notes = request_params.get("notes", "")

        doctor_note = DoctorNote(user=user, prescription=prescription, visit=visit, operation=operation,
                                 allergy=allergy, note=notes)
        doctor_note.save()

        return HttpResponse(json.dumps(doctor_note.to_dict()), content_type="application/json")
    elif request.method == "DELETE":
        # TODO: Implement this
        return HttpResponse(None, content_type="application/json")


"""
Old Views
"""


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
