from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
    if request.method == 'POST':
        dictionary = PyDictionary()
        word = request.POST['word']

        meaning = dictionary.meaning(word)

        context = {'word':word,'meaning':meaning}
    return render(request,'word.html',context)