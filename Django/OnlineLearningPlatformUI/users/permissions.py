from rest_framework.permissions import BasePermission,SAFE_METHODS
from courses.models import Course,Content
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role=='student'
    
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role=='teacher'

class IsTeacherOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        return request.user.role == 'teacher'

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if type(obj) == Course:
            return obj.teacher == request.user
        return obj.course.teacher == request.user

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        course_name = view.kwargs.get('name')
        try:
            course = Course.objects.get(name=course_name)
        except Course.DoesNotExist:
            return False
        
        return course.teacher == request.user