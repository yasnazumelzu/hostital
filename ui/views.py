from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UrniForm

def home(request):
    return render(request, "ui/home.html")

@login_required
def urni_crear(request):
    if request.method == "POST":
        form = UrniForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creado_por = request.user
            obj.save()
            messages.success(request, "Formulario URNI guardado correctamente.")
            return redirect("ui:urni_crear")
        messages.error(request, "Revisa los campos del formulario.")
    else:
        form = UrniForm()
    return render(request, "ui/urni_form.html", {"form": form})
