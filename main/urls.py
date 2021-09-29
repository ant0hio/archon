from django.urls import path
from . import views
from .views import *
from django_url_decr import url_decr
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required, permission_required


#urlpatterns = patterns(''
#    url_decr(r'^users/',
#             include('users.urls'),
#             decr=login_required))


urlpatterns = (
   # path('', url_decr(r'^foto/', include('foto.urls'), decr=login_required)),
    path('', views.index, name='home'),
    path('foto', views.foto, name='foto'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
)
