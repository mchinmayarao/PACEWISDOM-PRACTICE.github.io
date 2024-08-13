from django.db import models
from django.db.models import JSONField

class Employee(models.Model):

    empid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    summary = models.TextField()
    

    personal_info = JSONField()

    technical_skills = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()


    def __str__(self):
        return self.name

class EmployeeProject(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    contributions = models.TextField()

    def __str__(self):
        return f"{self.employee.name} - {self.project.name}"