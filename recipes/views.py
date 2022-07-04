from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Stefani',
    })


def sobre(request):
    return HttpResponse('sobre 1')


def contato(request):
    return HttpResponse('contato 1')
