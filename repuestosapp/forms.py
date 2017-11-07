from django import forms
from .models import Vehiculo, Repuesto

class VehiculoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Vehiculo
        fields = ('marca', 'duenio', 'anio', 'repuestos')

        def __init__ (self, *args, **kwargs):
            super(VehiculoForm, self).__init__(*args, **kwargs)
            self.fields["repuestos"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["repuestos"].help_text = "Ingrese los repuestos que necesita el vehiculo"
            self.fields["repuestos"].queryset = Repuesto.objects.all()
