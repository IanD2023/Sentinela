from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cadastros.controller.cadastrosController import Cadastros
from cadastros.controller.macsController import MACs
from dispositivos.controller.dispositivosController import Dispositivos
from senior.lojas import Lojas
from django.core.paginator import Paginator

@login_required
def home(request):

    return redirect(funcionario)

@login_required
def funcionario(request):

    nome = request.GET.get('nome')
    matricula = request.GET.get('matrícula')
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

    listaMacs=Cadastros().listarFuncionarioFiltro(nome=nome,matricula=matricula,mac=mac,loja=loja)  
    
    paginator = Paginator(listaMacs, 10)

    page_obj = paginator.get_page(numeroPagina)
    
    for list in page_obj:
        list.data_criacao=list.data_criacao.strftime("%d/%m/%Y")

    perfis=Cadastros().perfil()
    

    #return render(request,'funcionario/index.html',{'listamacs':listaMacs,"perfis":perfis})

    return render(request,'funcionario/index.html',{
        'page_obj':page_obj,"perfis":perfis,'total_registros':len(listaMacs),'filtro':filtro})


@login_required
def criarFuncionario(request):

    nome=request.POST.get("nome")
    perfil=request.POST.get("perfil")
    cpf=request.POST.get("cpf")
    matricula=request.POST.get("matricula")
    loja=request.POST.get("loja")
    setor=request.POST.get("setor")
    mac=request.POST.get("mac1")
    tipo=request.POST.get("tipo1")
    mac2=request.POST.get("mac2")
    tipo2=request.POST.get("tipo2")
    mac3=request.POST.get("mac3")
    tipo3=request.POST.get("tipo3")
    devices=Dispositivos("","").listar()   
    listaMacs=Cadastros().listarFuncionarios()
    ##lojas=Lojas.listarLojas()
    
    if nome:

        cadastro=Cadastros().criarcadastro(nome,perfil,cpf,matricula,"",loja,setor,request.user.first_name)
        macs=MACs(nome,cpf,matricula)

        if cadastro == True:
        
            if mac:
                if macs.criar(mac,tipo,1,perfil) != True: return render(request,"funcionario/index.html",{'devices':devices,'retorno':'1','msg':cadastro}) 
            if mac2: 
                if macs.criar(mac2,tipo2,2,perfil) != True: return render(request,"funcionario/index.html",{'devices':devices,'retorno':'1','msg':cadastro})
            if mac3:
                if macs.criar(mac3,tipo3,3,perfil) != True: return render(request,"funcionario/index.html",{'devices':devices,'retorno':'1','msg':cadastro})

            return redirect(funcionario)
        
        else:

            return render(request,"funcionario/index.html",{'devices':devices,'retorno':'1','msg':cadastro,'listamacs':listaMacs})

    return render(request,"funcionario/criar.html",{'devices':devices})