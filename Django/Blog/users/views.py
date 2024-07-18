from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views import View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

# Create your views here.
class SignUpView(View):
    
    
    template_name = "signUp.html"

    def get(self, request, *args, **kwargs):
        form =UserCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('signIn')

        return render(request, self.template_name, {"form": form})
    
    


class SignInView(LoginView):
    template_name = "signIn.html"
    # redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy("index")
    

# class SignOutView(LogoutView):
#     next_page = 'index'
    