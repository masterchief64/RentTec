from django.conf.urls import include, url
from django.conf import settings

from . import views
from propietarios.models import Propietario

urlpatterns = [
	url(r'^lista_casas/', views.lista_casas, name='lista_casas'),
	url(r'^publicar/', views.publicar, name='publicar'),

]

