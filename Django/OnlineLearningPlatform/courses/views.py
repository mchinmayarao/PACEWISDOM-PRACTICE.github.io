from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Course, Content,Enrollment
from .serializers import CourseSerializer, ContentSerializer,CourseCreateSerializer,ContentCreateSerializer
from users.permissions import IsTeacherOrReadOnly,IsOwnerOrReadOnly,IsOwner
from .permissions import IsEnrolledOrTeacher
from rest_framework import status


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
    
    def get_permissions(self):
        print("inside get_permisssions")
        if self.request.method in permissions.SAFE_METHODS:
            print("inside if")
            self.permission_classes = [permissions.IsAuthenticated, IsEnrolledOrTeacher,]
            
        else:
            self.permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly,]
        return super(ContentListCreateView, self).get_permissions()
    
    lookup_field = 'name'

    def list(self, request, *args, **kwargs): 
        course = Course.objects.get(name=kwargs['name'])
        contents = [content.title for content in course.content_set.all()]
        return Response({'contents':contents})

    def perform_create(self, serializer):
        name = self.kwargs['name']
        course = Course.objects.get(name=name)
        serializer.save(course=course)

class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = ContentSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            self.permission_classes = [permissions.IsAuthenticated, IsEnrolledOrTeacher,]
            
        else:
            self.permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly,]
        return super(ContentDetailView, self).get_permissions()
    
    lookup_field = 'title'
    def get_queryset(self):
        name = self.kwargs['name']
        course_id = Course.objects.get(name=name).course_id
        return Content.objects.filter(course=course_id)
    
class SubscribersListView(generics.ListAPIView):
        permission_classes = [permissions.IsAuthenticated,IsOwner,]
        def get(self, request, *args, **kwargs):
            course_name = kwargs.get('name')
            course = Course.objects.get(name=course_name)
            enrollment = Enrollment.objects.filter(course = course)
            subscribers = [{"name":user.student.name,"email":user.student.email} for user in enrollment]
            return Response({"subscribers":subscribers},status=status.HTTP_200_OK)