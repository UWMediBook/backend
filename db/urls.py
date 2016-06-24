from django.conf.urls import url, include, patterns
from rest_framework import routers
from db.views import mainViewSet, allergyViewSet, pastVisitViewSet, pastOperationViewSet, doctorNoteViewSet, \
    prescriptionViewSet, emergencyContactViewSet, primaryDoctorViewSet, allergyViewSet

from . import views

router = routers.DefaultRouter()
router.register(r'users', mainViewSet)
router.register(r'allergies', allergyViewSet)
router.register(r'pastvisits', pastVisitViewSet)
router.register(r'pastoperations', pastOperationViewSet)
router.register(r'doctorsnotes', doctorNoteViewSet)
router.register(r'prescriptions', prescriptionViewSet)
router.register(r'emergencycontacts', emergencyContactViewSet)
router.register(r'primarydoctor', primaryDoctorViewSet)

urlpatterns = router.urls
