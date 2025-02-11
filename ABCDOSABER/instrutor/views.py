from django.shortcuts import render
from django.http import HttpResponse
from instrutor.models import Instrutor
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<!DOCType='html'><html>")

def listar(request):
    lista_instrutor = Instrutor.objects.order_by("descricao")
    resposta = "<ul>"
    for instrutor in lista_instrutor:
        resposta += '<li>{0}</li>'.format(Instrutor)
        
    resposta += '</ul>'
    print(resposta)    
    return HttpResponse(resposta)


def show_mensagem(request):
    x = "M"
    nome = x + "Renan, tudo certo?"
    return HttpResponse(f"Bom dia!{nome}")

def detalhe_instrutor(request, instrutor_codigo):
    Instrutor = Instrutor.objects.get(pk=instrutor_codigo)
    return HttpResponse(Instrutor)