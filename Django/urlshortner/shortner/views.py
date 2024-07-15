from django.shortcuts import render,redirect
import uuid
from .models import Url
from django.http import HttpResponse
from .forms import UrlForm
# Create your views here.
def index(request):
    return render(request , 'index.html')

def create(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        
        if form.is_valid():
            link = form.cleaned_data['link']
            uid = str(uuid.uuid4())[:5]
            new_url = Url(link=link,uuid=uid)
            new_url.save()

            return render(request,'index.html',{'uid':'http://127.0.0.1:8000/' + uid})


def go(request,shortUrl):
    url_details = Url.objects.get(uuid=shortUrl)
    return redirect(url_details.link)