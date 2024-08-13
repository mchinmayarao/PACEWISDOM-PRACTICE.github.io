from rest_framework import serializers
from resumes.models import Employee, EmployeeProject, Project

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProject
        fields = '__all__'


class EmployeeProjectSerializer2(serializers.ModelSerializer):
    name = serializers.CharField(source='project.name')
    description = serializers.CharField(source='project.description')
    start_date = serializers.DateField(source='project.start_date')

    class Meta:
        model = EmployeeProject
        fields = ['name', 'description', 'start_date', 'role', 'contributions']

class EmployeeProjectDetailSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['empid', 'name', 'email', 'phone', 'summary', 'personal_info', 'technical_skills', 'projects']

    def get_projects(self, obj):
        employee_projects = EmployeeProject.objects.filter(employee=obj)
        return EmployeeProjectSerializer2(employee_projects, many=True).data


