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
    url(r'^users/$', views.users),
]
urlpatterns += router.urls
