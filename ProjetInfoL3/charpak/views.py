from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'public/index.html')

def index_arborescence(request):
    return render(request, 'arborescence/index_arborescence.html')