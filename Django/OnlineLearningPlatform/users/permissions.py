from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role=='student'
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role=='teacher'
