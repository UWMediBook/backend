from django.contrib import admin

from db.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Prescription)
admin.site.register(Allergy)
admin.site.register(Operation)
admin.site.register(Visit)
admin.site.register(EmergencyContact)
admin.site.register(PrimaryDoctor)
admin.site.register(DoctorNote)
