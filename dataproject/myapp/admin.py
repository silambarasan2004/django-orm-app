from django.contrib import admin
from .models import employee,EmployeeAdmin

admin.site.register(employee,EmployeeAdmin)