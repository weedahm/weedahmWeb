from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, User
from django.db import models

# GENDER = (
#     ('M', 'Man'),
#     ('W', 'Woman'),
# )

# def survey_file_directory_path(instance, filename):
#     return '{0}/{1}/{2}/{3}'.format(instance.created_date.year, instance.created_date.month, instance.created_date.day, filename)

# class Survey(models.Model):
#     created_date = models.DateTimeField("Survey Time of Patient", auto_now_add=True)
#     last_modified = models.DateTimeField("Last Modified Datetime", auto_now=True)
#     ref_file = models.FileField(upload_to=survey_file_directory_path)

#     def __str__(self):
#         return str(self.created_date)

class Person(AbstractUser):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, blank=True)
    # birthday = models.DateField(blank=True)
    age = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.first_name+self.last_name

    # class Meta:
    #     abstract = True

# class Patient(Person):
#     height = models.CharField(max_length=10)
#     weight = models.CharField(max_length=10)
#     survey = models.ForeignKey(Survey, on_delete=models.PROTECT)

# class Doctor(Person):
#     specialization = models.CharField(max_length=30)

