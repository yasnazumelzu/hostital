from django import forms
from .models import UrniRegistro

class UrniForm(forms.ModelForm):
    class Meta:
        model = UrniRegistro
        fields = [
            "madre_nombre", "madre_rut", "madre_edad",
            "semanas_gestacion", "controles_prenatales",
            "tipo_parto", "fecha_parto",
            "rn_peso_kg", "rn_talla_cm", "apgar_1", "apgar_5",
        ]
        widgets = {"fecha_parto": forms.DateInput(attrs={"type": "date"})}
