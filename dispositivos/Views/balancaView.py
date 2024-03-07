from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from dispositivos.controller.dispositivosController import Dispositivos
from cadastros.controller.macsController import MACs
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test


# @login_required
# def balanca(request):


#     lista_dispositivos=Dispositivos("","").listarBalancas()


#     return render(request,"balanca/index.html",{'lista_dispositivos':lista_dispositivos})


@user_passes_test(lambda u: u.is_superuser)
def balanca(request):

    loja = request.GET.get('loja')    
    setor = request.GET.get('setor')
    mac = request.GET.get('mac')
    filtro=""

    for x in dict(request.GET):

        if x != 'page' and request.GET[x] != "":
            
            filtro=[x,request.GET[x]] 

    if request.GET.get('page') == '':
        numeroPagina = 1   

    else:
        numeroPagina = request.GET.get('page')    

    lista_dispositivos=Dispositivos("","").listarBalancasFiltro(loja,setor,mac)  
    
    paginator = Paginator(lista_dispositivos, 10)

    page_obj = paginator.get_page(numeroPagina) 

    #lista_dispositivos=Dispositivos("","").listarBalancas()    

    return render(request,"balanca/index.html",{'page_obj':page_obj,'total_registros':len(lista_dispositivos),'filtro':filtro})

@user_passes_test(lambda u: u.is_superuser)
def criarBalanca(request):

    loja=request.POST.get("loja")
    setor=request.POST.get("setor")
    mac=request.POST.get("mac")

    if mac:

        if Dispositivos("","").criarBalanca(mac,loja,setor,request.user.first_name) == True:

            return redirect(balanca)
        
        else: 

            print("Mac já cadastrado")

    return render(request,"balanca/criar.html")


@user_passes_test(lambda u: u.is_superuser)
def editarBalanca(request,id):

    loja=request.POST.get("loja")
    setor=request.POST.get("setor")
    mac=request.POST.get("mac")

    if mac:

        if Dispositivos("","").editarColetor(id,loja,setor,mac,10,request.user.first_name) != False:

            return redirect(balanca)
   
    cadastro=Dispositivos("","").buscaIdColetor(id)

    return render(request,"balanca/editar.html",{'cadastro':cadastro})

@user_passes_test(lambda u: u.is_superuser)
def excluirBalanca(request,id):

    excluir=request.POST.get("excluir")

    if excluir:
        
        if Dispositivos("","").excluirColetor(id) != False:

                return redirect(balanca)

    cadastro=MACs("","","").buscaId(id)

    return render(request,"balanca/excluir.html",{'cadastro':cadastro})