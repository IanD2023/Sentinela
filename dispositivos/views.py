from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as Login,logout
from dispositivos.controller.dispositivosController import Dispositivos
from cadastros.controller.macsController import MACs
from datetime import datetime
# Create your views here.
@login_required
def dispositivos(request):

    lista_dispositivos=Dispositivos("","").listar()
    
    return render(request,"dispositivos/listardispositivos.html",{'lista_dispositivos':lista_dispositivos})

@login_required
def criarDispositivo(request):

    nome=request.POST.get("nome")
    vlan=request.POST.get("vlan")

    if nome:
        
        if Dispositivos(nome,vlan).criar() != False:

            return redirect(dispositivos)

    return render(request,"dispositivos/criar.html")
@login_required
def editarDispositivo(request,id):
    
    nome=request.POST.get("nome")
    vlan=request.POST.get("vlan")

    if nome:
        
        if Dispositivos(nome,vlan).editar(id) != False:

            return redirect(dispositivos)

    device=Dispositivos("","").buscaId(id)

    return render(request,"dispositivos/editar.html",{"device":device})

