from django.contrib import admin
from .models import Lab,Ambulance, Doctor,Patient,Appointment,PatientDischargeDetails
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class AmbulanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ambulance, AmbulanceAdmin)

class LabAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lab, LabAdmin)


class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)


