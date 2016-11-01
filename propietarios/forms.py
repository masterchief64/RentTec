from django import forms
from .models import Propietario

class PropietarioForm(forms.ModelForm):
	class Meta:
		model = Propietario
		fields = ('nombre','apellidos','telefono','whatsapp','direccion','email','password')