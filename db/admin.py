from django.contrib import admin

from db.models import user
from db.models import prescription
from db.models import allergy
from db.models import pastOperation
from db.models import pastVisit
from db.models import emergencyContact
from db.models import primaryDoctor
from db.models import doctorNote
# Register your models here.

admin.site.register(user)
admin.site.register(prescription)
admin.site.register(allergy)
admin.site.register(pastOperation)
admin.site.register(pastVisit)
admin.site.register(emergencyContact)
admin.site.register(primaryDoctor)
admin.site.register(doctorNote)
