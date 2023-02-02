from django.shortcuts import render, redirect
from .models import Usuario

def index(request):
    return render(request, 'usuarios/index.html')


def save_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        form_data = Usuario(name=name)
        form_data.save()

        return redirect('base')
    return render(request, 'base.html')