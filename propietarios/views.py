from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Propietario
from .forms import PropietarioForm
from casas.models import Casa

def registrar_propietario(request):
	if request.method == 'POST':
		form = PropietarioForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = PropietarioForm()
	return render(request, 'registrar_propietario.html', {'form': form} )

