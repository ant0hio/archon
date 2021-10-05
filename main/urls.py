from django.urls import path
from . import views
from .views import *
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required, permission_required
from django.views.static import serve
from django.conf import settings


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


urlpatterns = (
    path('', views.index, name='home'),
    path('foto/', views.foto, name='foto'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], protected_serve, {'document_root': settings.MEDIA_ROOT}),
)
