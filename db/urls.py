from django.conf.urls import url, include, patterns
from rest_framework import routers
from db.views import *

from . import views

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'allergies', AllergyViewSet)
router.register(r'visits', VisitViewSet)
router.register(r'operations', OperationViewSet)
router.register(r'notes', DoctorNoteViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'emergencycontacts', EmergencyContactViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    url(r'^get_users_api_view/$', UserAPIView.as_view()),
    url(r'^users/$', views.users),
]
urlpatterns += router.urls
