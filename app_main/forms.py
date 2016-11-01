from django import forms
from propietarios.models import Propietario
from alumnos.models import Alumno

class LoginPropietatioForm(forms.ModelForm):
	class Meta:
		model = Propietario
		fields = ('email', 'password')

class LoginAlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		fields = ('no_control', 'nip')