from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def foto(request):
    return render(request, 'main/foto.html')