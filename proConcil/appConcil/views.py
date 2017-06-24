from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formLey


def index(request):
    return HttpResponse("Index page.")


def calcular(request):
    if request.method == 'POST':
        form = formLey(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/calcular')
    else:
        form = formLey()
    return render(request, "calcular.html", {"form": form})

