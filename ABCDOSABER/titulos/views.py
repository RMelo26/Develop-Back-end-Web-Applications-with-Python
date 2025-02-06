from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<!DOCType html><html><body>olá eu estou no titulos</body></html>")

def listar(request):
    return HttpResponse("Lista de Tipos de Aividade")

def show_mensagem(request):
    x = "M"
    nome = x + "Renan, tudo certo?"
    return HttpResponse(f"Bom dia!{nome}")