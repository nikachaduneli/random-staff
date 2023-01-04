from django_filters import FilterSet
from .models import Applicant

class ApplicantFilter(FilterSet):
    class Meta:
        model = Applicant
        fields = ['fname', 'lname', 'birth_date', 'address', 'wanted_position',
                'wanted_city', 'mobile_number', 'color','applie_date']