from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf import settings


urlpatterns = (
    path('', views.index, name='home'),
    path('foto/', views.foto, name='foto'),
    path('video/', views.video, name='video'),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], views.protected_serve, {'document_root': settings.MEDIA_ROOT}),
    path('ups', views.view_ups, name='ups'),
)
