from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet,ProjectViewSet,EmployeeProjectViewSet,EmployeeProjectDetailView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'employee_project', EmployeeProjectViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/employee_project_detail/',EmployeeProjectDetailView.as_view(),name="employee_project_detail"),
]