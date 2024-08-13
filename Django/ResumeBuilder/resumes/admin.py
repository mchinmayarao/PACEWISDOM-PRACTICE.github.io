from django.contrib import admin
from .models import Employee,EmployeeProject,Project
# Register your models here.
admin.site.register(EmployeeProject)
admin.site.register(Employee)
admin.site.register(Project)