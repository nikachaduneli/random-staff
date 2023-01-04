from django.contrib import admin
from .models import Applicant


class ApplicantAdmin(admin.ModelAdmin):
    search_fields = ['fname', 'lname', 'birth_date', 'wanted_position', 'wanted_city']
    list_filter = ['applie_date', 'wanted_position', 'wanted_city']


admin.site.register(Applicant, ApplicantAdmin)