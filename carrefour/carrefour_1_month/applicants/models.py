from django.utils import timezone
from django.db import models


class Applicant(models.Model):
    fname = models.CharField(max_length=200, null=False)
    lname = models.CharField(max_length=200, null=False)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=200, null=False)
    wanted_position = models.CharField(max_length=200, null=False)
    wanted_city = models.CharField(max_length=200, null=False)
    applie_date = models.DateField(default=timezone.now)
    mobile_number = models.CharField(max_length=30, default='000000000', null=False)
    color = models.CharField(max_length=100, default='#FFFFFF')

    def __str__(self) -> str:
        return f'{self.fname} {self.lname}'


class Comment(models.Model):
    content = models.CharField(max_length=400, default='testing')
    applicant = models.ForeignKey(Applicant, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
