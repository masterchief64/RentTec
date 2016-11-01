from django import forms
from .models import Casa

class CasaForm(forms.ModelForm):
	class Meta:
		model = Casa
		fields = ('tipo_casa','renta','pago','direccion','cuartos','banios','pisos','servicios','negocios_cercanos','tiempo_tec','rutas_tec','casa_frente','casa_cuarto','casa_banio','casa_otra','propietario')
		casa_frente = forms.ImageField()
		casa_cuarto = forms.ImageField()
		casa_banio = forms.ImageField()
		casa_otra = forms.ImageField()
