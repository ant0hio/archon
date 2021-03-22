from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('foto', views.foto, name='foto'),
]
