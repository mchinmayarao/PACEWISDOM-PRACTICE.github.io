from django.contrib.auth import authenticate
from .models import User
from django.views.generic import CreateView
from django.views import View
from .forms import LoginForm,SignupForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course,Enrollment
# Create your views here.

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                form = login(request, user)
                messages.success(request, f' welcome {user.name}!!')
                return redirect('index')
            else:
                messages.info(request, f'invalid credentials')
                return redirect('login')

class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login') 
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your account has been created successfully! You can now log in.')
        return response
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, f'Logout successfull.')
        return redirect('index')
    
class DashboardView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        if request.user.role == "teacher":
            courses = Course.objects.filter(teacher=request.user)
            
            enrollments = Enrollment.objects.filter(course__in =courses)
            subscribers = [{'name':item.student.name,'course':item.course.name} for item in enrollments]

            subscribed_courses = Enrollment.objects.filter(student = request.user)

            return render(request,'teacher_dashboard.html',{"subscribers":subscribers,"courses":courses,"subscribed_courses":subscribed_courses})
        else:
            subscribed_courses = Enrollment.objects.filter(student = request.user)
            return render(request,'student_dashboard.html',{"subscribed_courses":subscribed_courses})
