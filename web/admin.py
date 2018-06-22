from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person

admin.site.register(Person, UserAdmin)
# admin.site.register(Patient)
# admin.site.register(Doctor)
# admin.site.register(Survey)
# Register your models here.
