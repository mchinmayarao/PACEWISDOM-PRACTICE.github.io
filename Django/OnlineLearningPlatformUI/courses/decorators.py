from django.core.exceptions import PermissionDenied
from functools import wraps
from .models import Course,Enrollment
from django.http import HttpResponse
def is_teacher(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'teacher':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("<h1> You are not a teacher")
    return _wrapped_view

def is_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        course = Course.objects.get(name=kwargs['name'])
        if request.user == course.teacher:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("<h1> You are not the owner")
    return _wrapped_view

def is_enrolled_or_teacher(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        course = Course.objects.get(name=kwargs['name'])
        if request.user.is_authenticated:
            if request.user == course.teacher:
                return view_func(request, *args, **kwargs)
            try:
                enrollment = Enrollment.objects.get(student=request.user, course=course)
                enrollment.update_status()  # Ensure status is up-to-date
                if enrollment.status == 'active':
                    return view_func(request, *args, **kwargs)
            except Enrollment.DoesNotExist:
                pass
        return HttpResponse("<h1>Purchase the course </h1>")
    return _wrapped_view
