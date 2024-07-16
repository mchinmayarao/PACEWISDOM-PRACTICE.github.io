from django.shortcuts import render,redirect
from .models import ToDoList
# Create your views here.
def index(request):
   if request.method == 'POST':
      new_todo = ToDoList(item = request.POST['item'])
      new_todo.save()
      return redirect('/')
   
   return render(request,'index.html',{"todos":ToDoList.objects.all()})

def delete(request,itemId):
   item = ToDoList(id = itemId)
   item.delete()
   return redirect('/')