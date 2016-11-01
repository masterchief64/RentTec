from django.shortcuts import render, redirect
from .models import Casa
from .forms import CasaForm


def lista_casas(request):
	casas = Casa.objects.all()
	return render(request, 'lista_casas.html', {'casas': casas})

def publicar(request):
	if request.method == 'POST':
		form = CasaForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = CasaForm()
	return render(request, 'registrar.html', {'form':form} )
