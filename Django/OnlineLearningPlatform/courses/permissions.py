from rest_framework.permissions import BasePermission,SAFE_METHODS
from .models import Enrollment, Course,Content

class IsEnrolledOrTeacher(BasePermission):
       
    def has_permission(self, request, view):
        course_name = view.kwargs.get('name')
        try:
            course = Course.objects.get(name=course_name)
        except Course.DoesNotExist:
            return False
        
        is_enrolled = Enrollment.objects.filter(course=course, student=request.user).exists()
        is_teacher = course.teacher == request.user
        
        return is_enrolled or is_teacher
        
        
