from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .ups import *
from . import ups

from .forms import *
from .models import *
from .utils import *
# Create your views here.
from django.contrib.auth import logout, login


def index(request):
    return render(request, 'main/index.html')

@login_required
def foto(request):
    return render(request, 'main/foto.html')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


def ups_dash(request):
    return render(request, 'main/ups_dash.html', {})


def view_ups(request):
    output = ups.upsresult
    return render(request, 'main/ups_results.html', {'output': output})

