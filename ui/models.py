from django.conf import settings
from django.db import models

class Perfil(models.Model):
    ROL_CHOICES = [
        ("medico", "Médico"),
        ("enfermera", "Enfermera"),
        ("administrativo", "Administrativo"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="perfil")
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default="administrativo")

    def __str__(self):
        return f"{self.user.username} ({self.get_rol_display()})"


class UrniRegistro(models.Model):
    madre_nombre = models.CharField(max_length=120)
    madre_rut = models.CharField(max_length=12, blank=True)
    madre_edad = models.PositiveIntegerField(null=True, blank=True)
    semanas_gestacion = models.PositiveIntegerField(null=True, blank=True)
    controles_prenatales = models.PositiveIntegerField(null=True, blank=True)
    tipo_parto = models.CharField(max_length=20, choices=[("vaginal", "Parto vaginal"), ("cesarea", "Cesárea")])
    fecha_parto = models.DateField(null=True, blank=True)
    rn_peso_kg = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    rn_talla_cm = models.PositiveIntegerField(null=True, blank=True)
    apgar_1 = models.PositiveIntegerField(null=True, blank=True)
    apgar_5 = models.PositiveIntegerField(null=True, blank=True)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"URNI {self.id} - {self.madre_nombre}"



