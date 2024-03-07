from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from cadastros.controller.cadastrosController import Cadastros
from cadastros.controller.macsController import MACs
from dispositivos.controller.dispositivosController import Dispositivos
from django.core.paginator import Paginator

# @login_required
# def visitante(request):

#     listaMacs=Cadastros().listarVisitante()

#     for list in listaMacs:
#         list.data_criacao=list.data_criacao.strftime("%d/%m/%Y")

#     perfis=Cadastros().perfil()

#     return render(request,'visitante/index.html',{'listamacs':listaMacs,"perfis":perfis})


@login_required
def visitante(request):

    nome = request.GET.get('nome')
    cpf = request.GET.get('cpf')
    mac = request.GET.get('mac')
    loja = request.GET.get('loja')
    filtro=""

    for x in dict(request.GET):

        if x != 'page' and request.GET[x] != "":
            
            filtro=[x,request.GET[x]] 

    
    if request.GET.get('page') == '':
        numeroPagina = 1   

    else:
        numeroPagina = request.GET.get('page')    

    listaMacs=Cadastros().listarVisitanteFiltro(nome=nome,mac=mac,cpf=cpf)  
    
    paginator = Paginator(listaMacs, 10)

    page_obj = paginator.get_page(numeroPagina)

    #listaMacs=Cadastros().listarVisitanteFiltro(nome=nome,mac=mac,cpf=cpf)

    for list in page_obj:
        list.data_criacao=list.data_criacao.strftime("%d/%m/%Y")

    perfis=Cadastros().perfil()

    return render(request,'visitante/index.html',{'page_obj':page_obj,"perfis":perfis,'total_registros':len(listaMacs),"filtro":filtro})


@login_required
def criarVisitante(request):

    nome=request.POST.get("nome")
    perfil=request.POST.get("perfil")
    cpf=request.POST.get("cpf")
    matricula=request.POST.get("matricula")
    solicitante=request.POST.get("solicitante")
    tempo_acesso=request.POST.get("tempo_acesso")
    loja=request.POST.get("loja")
    mac=request.POST.get("mac1")
    tipo=request.POST.get("tipo1")
    mac2=request.POST.get("mac2")
    tipo2=request.POST.get("tipo2")
    mac3=request.POST.get("mac3")
    tipo3=request.POST.get("tipo3")
    devices=Dispositivos("","").listar()
    listaMacs=Cadastros().listarVisitante()
    
    if nome:

        cadastro=Cadastros().criarcadastro(nome,perfil,cpf,matricula,tempo_acesso,loja,solicitante,request.user.first_name)
        macs=MACs(nome,cpf,matricula)

        if cadastro == True:

            if mac: macs.criar(mac,tipo,1,perfil)
            if mac2: macs.criar(mac2,tipo2,2,perfil)
            if mac3: macs.criar(mac3,tipo3,3,perfil)

            return redirect(visitante)
        
        else:

            return render(request,"visitante/index.html",{'listamacs':listaMacs,'retorno':'1','msg':cadastro})         

    return render(request,"visitante/criar.html",{'devices':devices})