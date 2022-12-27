from django.db import models
from django.contrib import admin
# Create your models here.
class employee(models.Model):
    empid=models.CharField(primary_key=True, max_length=4,help_text='Employee ID')
    ename=models.CharField(max_length=50)
    degree=models.CharField(max_length=30)
    post=models.CharField(max_length=20)
    salary=models.IntegerField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('empid','ename','degree','post','salary')