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
    url(r'^authenticate/$', views.authenticate),
    url(r'^users/$', views.users),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.users_by_id),
    url(r'^users/(?P<user_id>[0-9]+)/emergency_contacts/$', views.emergency_contacts_by_user_id),
    url(r'^users/(?P<user_id>[0-9]+)/allergies/$', views.allergies_by_user_id),
    url(r'^users/(?P<user_id>[0-9]+)/operations/$', views.operations_by_user_id),
    url(r'^users/(?P<user_id>[0-9]+)/visits/$', views.visits_by_user_id),
    url(r'^users/(?P<user_id>[0-9]+)/prescriptions/$', views.prescriptions_by_user_id),
    url(r'^users/(?P<user_id>[0-9]+)/physicians/$', views.physicians_by_user_id),
    url(r'^users/(?P<email>\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3})/$', views.users_by_email),
    url(r'^doctors/$', views.doctors),
    url(r'^doctors/(?P<doctor_id>[0-9]+)/$', views.doctors_by_id),
    url(r'^emergency_contacts/$', views.emergency_contacts),
    url(r'^emergency_contacts/(?P<contact_id>[0-9]+)/$', views.emergency_contacts_by_id),
    url(r'^allergies/$', views.allergies),
    url(r'^allergies/(?P<allergy_id>[0-9]+)/$', views.allergies_by_id),
    url(r'^prescriptions/$', views.prescriptions),
    url(r'^prescriptions/(?P<prescription_id>[0-9]+)/$', views.prescriptions_by_id),
    url(r'^operations/$', views.operations),
    url(r'^operations/(?P<operation_id>[0-9]+)/$', views.operations_by_id),
    url(r'^visits/$', views.visits),
    url(r'^visits/(?P<visit_id>[0-9]+)/$', views.visits_by_id),
    url(r'^physicians/$', views.physicians),
    url(r'^physicians/(?P<physician_id>[0-9]+)/$', views.physicians_by_id),
    url(r'^doctor_notes/$', views.doctor_notes),

]
urlpatterns += router.urls
