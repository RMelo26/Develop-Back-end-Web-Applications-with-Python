from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Olá, eu sou a visão do request 'index'.")

def teste(request):
    return HttpResponse("Eu sou um teste.")