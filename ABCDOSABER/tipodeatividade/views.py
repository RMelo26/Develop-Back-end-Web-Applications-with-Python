from django.shortcuts import render
from django.http import HttpResponse
from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def index(request):
    return HttpResponse("<!DOCType='html'><html>")

def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.order_by("descricao")
    resposta = "<ul>"
    for tipodeatividade in lista_tipodeatividade:
        resposta += '<li>{0}</li>'.format(tipodeatividade)
        
    resposta += '</ul>'
    print(resposta)    
    return HttpResponse(resposta)


def show_mensagem(request):
    x = "M"
    nome = x + "Renan, tudo certo?"
    return HttpResponse(f"Bom dia!{nome}")

def detalhe_tipodeatividade(request, tipodeatividade_codigo):
    tipodeatividade = TipoDeAtividade.objects.get(pk=tipodeatividade_codigo)
    return HttpResponse(tipodeatividade)