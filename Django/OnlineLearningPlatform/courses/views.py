from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Course, Content
from .serializers import CourseSerializer, ContentSerializer,CourseCreateSerializer,ContentCreateSerializer
from users.permissions import IsTeacherOrReadOnly,IsOwnerOrReadOnly

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = [IsTeacherOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(teacher = self.request.user)

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'name'

class ContentListCreateView(generics.ListCreateAPIView):
    serializer_class = ContentCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeacherOrReadOnly]
    lookup_field = 'name'

    def get_queryset(self):
        name = self.kwargs['name']
        course_id = Course.objects.get(name=name).course_id
        return Content.objects.filter(course=course_id)

    def perform_create(self, serializer):
        name = self.kwargs['name']
        course = Course.objects.get(name=name)
        serializer.save(course=course)

class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        name = self.kwargs['name']
        course_id = Course.objects.get(name=name).course_id
        return Content.objects.filter(course=course_id)