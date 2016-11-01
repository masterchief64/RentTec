from django.conf.urls import include, url
from django.conf import settings

from . import views
from propietarios.models import Propietario

urlpatterns = [
	url(r'^registrar_propietario/', views.registrar_propietario, name='registrar_propietario'),

]

