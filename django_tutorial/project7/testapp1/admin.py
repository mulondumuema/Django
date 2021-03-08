from django.contrib import admin
from .models import Registration

# Register your models here.


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'city', 'email']

admin.site.register(Registration, RegistrationAdmin)
