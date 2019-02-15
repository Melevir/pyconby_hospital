from django.contrib import admin

from . import models


class PatientAdmin(admin.ModelAdmin):
    pass


class DoctorAdmin(admin.ModelAdmin):
    pass


class VisitAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Visit, VisitAdmin)
