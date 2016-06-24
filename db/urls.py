from django.conf.urls import url, include, patterns
from rest_framework import routers
from db.views import *

from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'allergies', AllergyViewSet)
router.register(r'visits', VisitViewSet)
router.register(r'operations', OperationViewSet)
router.register(r'notes', DoctorNoteViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'emergencycontacts', EmergencyContactViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = router.urls
