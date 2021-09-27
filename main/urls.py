from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='home'),
    path('foto', views.foto, name='foto'),
    path('login/', LoginUser.as_view(), name='login'),
]
