from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from dispositivos.controller.dispositivosController import Dispositivos
from cadastros.controller.macsController import MACs
from django.core.paginator import Paginator

# @login_required
# def coletores(request):

#     lista_dispositivos=MACs("","","").listarDispositivo(27)
    
#     return render(request,"coletores/index.html",{'lista_dispositivos':lista_dispositivos})

@login_required
def coletores(request):

    loja = request.GET.get('loja')
    mac = request.GET.get('mac')
    setor = request.GET.get('setor')    
    filtro=""

    for x in dict(request.GET):

        if x != 'page' and request.GET[x] != "":
            
            filtro=[x,request.GET[x]]   

    #lista_dispositivos=MACs().listarDispositivo(27)

    if request.GET.get('page') == '':
        numeroPagina = 1   

    else:
        numeroPagina = request.GET.get('page')    

    lista_dispositivos=MACs('','','').listarDispositivoFiltro(3,loja,setor,mac)  
    
    paginator = Paginator(lista_dispositivos, 10)

    page_obj = paginator.get_page(numeroPagina)    
    
    return render(request,"coletores/index.html",{'page_obj':page_obj,'total_registros':len(lista_dispositivos),'filtro':filtro})

@login_required
def criarColetor(request):

    loja=request.POST.get("loja")
    setor=request.POST.get("setor")
    mac=request.POST.get("mac")

    if mac:

        if Dispositivos("",27).criarColetor(mac,loja,setor,request.user.first_name) != False:

            return redirect(coletores)

    return render(request,"coletores/criar.html")    
        

@login_required
def editarColetor(request,id):

    loja=request.POST.get("loja")
    setor=request.POST.get("setor")
    mac=request.POST.get("mac")

    if mac:

        if Dispositivos("",27).editarColetor(id,loja,setor,mac,3,request.user.first_name) != False:

            return redirect(coletores)
   
    cadastro=Dispositivos("","").buscaIdColetor(id)

    return render(request,"coletores/editar.html",{'cadastro':cadastro})

@login_required
def excluirColetor(request,id):

    excluir=request.POST.get("excluir")

    if excluir:
        
        if Dispositivos("","").excluirColetor(id) != False:

                return redirect(coletores)

    cadastro=MACs("","","").buscaId(id)    

    return render(request,"coletores/excluir.html",{'cadastro':cadastro})        
        