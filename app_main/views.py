from django.shortcuts import render, render_to_response, redirect
from propietarios.models import Propietario
from casas.models import Casa

from .forms import LoginPropietatioForm, LoginAlumnoForm

def home(request):
	propietario = Propietario.objects.all()
	return render(request, 'index.html', {'propietario': propietario} )

def login_propietario(request):
	if request.method == 'POST':
		form = LoginPropietatioForm(request.POST)
		if request.POST['email'] == 'yosoy280@gmail.com' and request.POST['password'] == 'choripan':
			return redirect('/publicar_casa/')
		else:
			return redirect('/login_propietario/')
	else:
		form = LoginPropietatioForm()
	return render(request, 'login_propietario.html', {'form':form})

def login_alumno(request):
	if request.method == 'POST':
		form = LoginPropietatioForm(request.POST)
		if request.POST['no_control'] == '14590223' and request.POST['nip'] == '5084':
			return redirect('/casas/lista_casas/')
		else:
			return redirect('/login_alumno/')
	else:
		form = LoginAlumnoForm()
	return render(request, 'login_alumno.html', {'form': form} )


def publicar_casa(request):
	casas = Casa.objects.all()
	return render(request, 'publicar_casa.html', {'casas':casas} )