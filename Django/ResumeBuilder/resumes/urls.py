from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('employee/', views.employee_details, name='employee_details'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
]


