from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('signUp/', views.SignUpView.as_view(), name='signUp'),
    path('signIn/', views.SignInView.as_view(), name='signIn'),
    path('signOut/', LogoutView.as_view(next_page='index'), name='signOut'),
]
