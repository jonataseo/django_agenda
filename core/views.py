from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.
def retorna_descricao(request, titulo_evento):
    descricao = Evento.objects.get('titulo' == titulo_evento).descricao
    return HttpResponse("Local do evento: {}".format(descricao))
#
# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request,'agenda.html', response)