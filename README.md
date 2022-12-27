# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
create application 

### STEP 2:
create model.py and admin.py
create myapp

### STEP 3:
make migrations and migrate
finally runserver 0:8000

Write your own steps

## PROGRAM

model.py
```python
from django.db import models
from django.contrib import admin

class employee(models.Model):
    empid=models.CharField(primary_key=True, max_length=4,help_text='Employee ID')
    ename=models.CharField(max_length=50)
    degree=models.CharField(max_length=30)
    post=models.CharField(max_length=20)
    salary=models.IntegerField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('empid','ename','degree','post','salary')
```
admin.py
```python
from django.contrib import admin
from .models import employee,EmployeeAdmin

admin.site.register(employee,EmployeeAdmin)
```

## OUTPUT

Include the screenshot of your admin page.
![Screenshot of admin page](./images/employeecreate.png)
![Screenshot of primary_key_check](./images/employeecreatesameno.png)

## RESULT

To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).
