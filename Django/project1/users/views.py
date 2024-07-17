from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request,"users/register.html",{'form':form})

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username= username,password=password)
        if user is not None:
            return redirect('posts:list')
        else:
            return render(request,"users/login.html",{'form':AuthenticationForm()})
        
    else:
        form = AuthenticationForm()
        return render(request, "users/login.html",{'form':form})
    
