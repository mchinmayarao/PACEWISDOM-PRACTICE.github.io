from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from resumes.models import Employee,EmployeeProject,Project
from .serializers import EmployeeSerializer,EmployeeProjectSerializer,ProjectSerializer,EmployeeProjectDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,filters

# Create your views here.

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','empid']

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EmployeeProjectViewSet(ModelViewSet):
    queryset = EmployeeProject.objects.all()
    serializer_class = EmployeeProjectSerializer

class EmployeeProjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        empid = self.request.query_params.get('empid')
        
        if empid is None:
            return Response({"error": "Employee ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            employee = Employee.objects.get(empid=empid)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeProjectDetailSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

