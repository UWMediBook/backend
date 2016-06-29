from django.conf.urls import url, include, patterns
from rest_framework import routers
from db.views import *

from . import views

router = routers.DefaultRouter()
router.register(r'userviewset', UserViewSet)
router.register(r'allergyviewset', AllergyViewSet)
router.register(r'visitviewset', VisitViewSet)
router.register(r'operationviewset', OperationViewSet)
router.register(r'noteviewset', DoctorNoteViewSet)
router.register(r'prescriptionviewset', PrescriptionViewSet)
router.register(r'emergencycontactviewset', EmergencyContactViewSet)
router.register(r'doctorviewset', DoctorViewSet)

urlpatterns = [
    url(r'^users/$', views.Users.as_view()),
    url(r'^doctors/$', views.Doctors.as_view()),
    url(r'^emergency_contacts/$', views.EmergencyContacts.as_view()),
    url(r'^allergies/$', views.Allergies.as_view()),
    url(r'^prescriptions/$', views.Prescriptions.as_view()),
    url(r'^operations/$', views.Operations.as_view()),
    url(r'^visits/$', views.Visits.as_view()),
    url(r'^doctor_notes/$', views.DoctorNotes.as_view()),

]
urlpatterns += router.urls
