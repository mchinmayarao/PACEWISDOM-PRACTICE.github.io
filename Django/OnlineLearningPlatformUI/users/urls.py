from django.urls import path

from .views import SignUpView,LogoutView,LoginView,DashboardView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/',DashboardView.as_view(),name='dashboard')
]