from __future__ import unicode_literals

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from jsonfield import JSONField

GENDER = (
    ('M', 'Man'),
    ('W', 'Woman'),
)

SPECIALIZATION = (
    ('KMD', '한의사'),
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, contact_number, date_of_birth=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            contact_number=contact_number,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, contact_number, password, date_of_birth=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            contact_number=contact_number,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    contact_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Doctor(User):
    specialization = models.CharField(max_length=30, choices=SPECIALIZATION)

def survey_file_directory_path(instance, filename):
    return 'surveys/{0}/{1}/{2}/{3}'.format(instance.created_date.year, instance.created_date.month, instance.created_date.day, filename)

class Survey(models.Model):
    """
    Arguments:
        ref_file
    """
    created_date = models.DateTimeField("Survey Time of Patient", auto_now_add=True)
    last_modified = models.DateTimeField("Last Modified Datetime", auto_now=True)
    survey_json = JSONField()

    def __str__(self):
        return str(self.created_date)

    # def save(self, *args, **kwargs):
    #     self.ref_file = 

class Patient(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT, blank=True, null=True)
    receiving_date = models.DateField(auto_now_add=True)
    # contact_number = models.CharField(max_length=20)
    surgical_history = models.TextField(blank=True)
    medicine_history = models.TextField(blank=True)

    def __str__(self):
        return self.name