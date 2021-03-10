from django.contrib import admin
from .models import Employee
from django.contrib.auth.models import Group, User



class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid', 'ename', 'ecity']

admin.site.site_header="Welcome To Uplatz"



# Register your models here.
admin.site.register(Employee, EmployeeAdmin)

# to unregister
admin.site.unregister(Group)
admin.site.unregister(User)
# admin.site.unregister(Employee)