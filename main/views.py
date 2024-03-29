from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .ups import upsresult
from django.views.static import serve


def index(request):
    return render(request, 'main/index.html')


@login_required
def foto(request):
    return render(request, 'main/foto.html')


def temp(request):
    return render(request, 'main/temp.html')


@login_required
def view_ups(request):
    return render(request, 'main/ups_results.html', {'ups': upsresult()})


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)
