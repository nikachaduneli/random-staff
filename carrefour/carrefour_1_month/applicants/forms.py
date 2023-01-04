from django import forms
from .models import Applicant

class ApplicantForm(forms.Form):
    class Meta:
        model = Applicant
        fields = '__all__'