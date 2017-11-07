from django.shortcuts import render

from django.contrib import messages
from .forms import VehiculoForm
from repuestosapp.models import Vehiculo, Asignacion

def vehiculo_nuevo(request):
    if request.method == "POST":
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            vehiculo = Vehiculo.objects.create(marca=formulario.cleaned_data['marca'], duenio = formulario.cleaned_data['duenio'], anio = formulario.cleaned_data['anio'])
            for repuesto_id in request.POST.getlist('repuestos'):
                asignacion = Asignacion(repuesto_id=repuesto_id, vehiculo_id = vehiculo.id)
                Asginacion.save()
            messages.add_message(request, messages.SUCCESS, 'Vehiculo Guardado Exitosamente')
    else:
        formulario = VehiculoForm()
    return render(request, 'repuestosapp/vehiculo_editar.html', {'formulario': formulario})
