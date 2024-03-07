from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as Login,logout
from cadastros.controller.cadastrosController import Cadastros
from cadastros.controller.macsController import MACs
from dispositivos.controller.dispositivosController import Dispositivos
from cadastros.controller.usuariosController import Usuarios
from cadastros.controller.validacoesController import Validacoes
from .radius.controller.radiusController import RADCHECK,RADREPLY
from .Views.usuariosView import *
from .Views.funcionarioView import *
from .Views.VisitanteView import *
from senior.senior import ConsultarMatricula
from datetime import datetime

# Create your views here.
def login(request):

    usuario=request.POST.get("login")
    senha=request.POST.get("senha")

    if usuario:

        try:

            user=authenticate(request,username=usuario, password=senha)

            Login(request,user)

            return redirect(home)
        
        except:

            return render(request,'login/index.html',{"retorno":"Usuário ou senha incorretos"})

        
    logout(request)

    return render(request,'login/index.html')


@login_required
def editar(request,id):

    nome=request.POST.get("nome")
    perfil=request.POST.get("perfil")
    tempo_acesso=request.POST.get("tempo_acesso")
    cpf=request.POST.get("cpf")
    solicitante=request.POST.get("solicitante")
    matricula=request.POST.get("matricula")
    loja=request.POST.get("loja")
    setor=request.POST.get("setor")
    mac=request.POST.get("mac1")
    tipo=request.POST.get("tipo1")
    mac2=request.POST.get("mac2")
    tipo2=request.POST.get("tipo2")
    mac3=request.POST.get("mac3")
    tipo3=request.POST.get("tipo3")
    cadastro=Cadastros().buscaId(id)
    macs=MACs(cadastro.nome,cadastro.cpf,cadastro.matricula)
    dispostivos_cadastrados=macs.dispositivos()
    perfis=Cadastros().perfil()
    devices=Dispositivos("","").listar()
    id_radcheck=RADCHECK.buscarMac(dispostivos_cadastrados)
    id_radreply=RADREPLY.buscarMac(dispostivos_cadastrados)

    if nome:

        Cadastros().editar(id,nome,perfil,cpf,mac,matricula,tipo,loja,setor,tempo_acesso,solicitante,request.user.first_name)
        macs=MACs(nome,cpf,matricula)

        if mac or mac == "":
            mac_id=request.POST.get("mac_id_1")
            mac_radcheck=request.POST.get("mac_radcheck_1")
            if mac == "":
                macs.deletar(mac_id)
                RADREPLY.excluirMac(mac_radcheck)
                RADCHECK.excluirMac(mac_radcheck)
            else: 
                RADCHECK.editar(mac_radcheck,mac,tipo,perfil)
                macs.editar(mac_id,mac,tipo,1,perfil)
            
        if mac2 or mac2 == "":
            mac_id_2=request.POST.get("mac_id_2")
            mac_radcheck_2=request.POST.get("mac_radcheck_2")
            if mac2 == "":
                macs.deletar(mac_id_2)
                RADREPLY.excluirMac(mac_radcheck_2)
                RADCHECK.excluirMac(mac_radcheck_2)
            else: 
                RADCHECK.editar(mac_radcheck_2,mac2,tipo2,perfil)
                macs.editar(mac_id_2,mac2,tipo2,2,perfil)

        if mac3 or mac3 == "": 
            mac_id_3=request.POST.get("mac_id_3")
            mac_radcheck_3=request.POST.get("mac_radcheck_3")
            if mac3 == "":
                macs.deletar(mac_id_3)
                RADREPLY.excluirMac(mac_radcheck_3)
                RADCHECK.excluirMac(mac_radcheck_3)

            else: 
                RADCHECK.editar(mac_radcheck_3,mac3,tipo3,perfil)
                macs.editar(mac_id_3,mac3,tipo3,3,perfil)

        if cadastro.perfil == 2: 

            return redirect(visitante)   

        return redirect(home)

    if cadastro.perfil == 2:

        return render(request,"visitante/editar.html",{
        'cadastro':cadastro,'dispositivos':dispostivos_cadastrados,'perfis':perfis,
        'devices':devices,'qtd_dispositivos':len(dispostivos_cadastrados),'retorno':'1',
        'id_radcheck':id_radcheck,'id_radreply':id_radreply})
          
    return render(request,"funcionario/editar.html",{
        'cadastro':cadastro,'dispositivos':dispostivos_cadastrados,'perfis':perfis,
        'devices':devices,'qtd_dispositivos':len(dispostivos_cadastrados),
        'id_radcheck':id_radcheck,'id_radreply':id_radreply})


@login_required
def criar(request):

    nome=request.POST.get("nome")
    perfil=request.POST.get("perfil")
    cpf=request.POST.get("cpf")
    matricula=request.POST.get("matricula")
    mac=request.POST.get("mac1")
    tipo=request.POST.get("tipo1")
    mac2=request.POST.get("mac2")
    tipo2=request.POST.get("tipo2")
    mac3=request.POST.get("mac3")
    tipo3=request.POST.get("tipo3")
    
    if nome:

        cadastro=Cadastros().criarcadastro(nome,perfil,cpf,matricula)
        macs=MACs(nome,cpf,matricula)

        if cadastro == True:

            if mac: macs.criar(mac,tipo,1)
            if mac2: macs.criar(mac2,tipo2,2)
            if mac3: macs.criar(mac3,tipo3,3)

            return render(request,"home/criarcadastro.html")
        
        else:

            print(cadastro)


    devices=Dispositivos("","").listar()          

    return render(request,"home/criarcadastro.html",{'devices':devices})


@login_required
def excluirCadastro(request,id):

    excluir=request.POST.get("excluir")
    cadastro=Cadastros().buscaId(id)
    perfil=cadastro.perfil

    if excluir:

        if Cadastros().excluir(id) != False:

            if perfil == 2:
                return redirect(visitante) 
            return redirect(funcionario) 

    return render(request,"home/excluir.html",{'cadastro':cadastro})

@login_required
def ajustes(request):

    return render(request,"home/ajustes.html")

@login_required
def buscarColaborador(request,id):

    resulta = ConsultarMatricula.Consultar(id)

    if ConsultarMatricula.ConsultarMatricula(id) == False:

        if resulta:

            dadosFuncionario=f"{resulta.nome}-{resulta.cpf}-{resulta.ativo}-{resulta.codigodafilial}-{resulta.nomedosetor}"

           ## print(dadosFuncionario)
            return HttpResponse(dadosFuncionario)
        
        return HttpResponse("500-Matrícula não encontrada")

    return HttpResponse("500-Matrícula já cadastrada-"+resulta.nome)

@login_required
def verificacoes(request,id):

    nome_validacao=id.split('@')[0]
    dado=id.split('@')[1]
    

    if nome_validacao == "validar_mac":
        
        validacao=Validacoes.validarMac(dado)

        return HttpResponse(validacao)
    
    if nome_validacao == "validar_mac_existente":

        validacao=Validacoes.validarMacExistente(dado,id.split('@')[2])

        return HttpResponse(validacao)
    
    if nome_validacao == "validar_nome":

        validacao=Validacoes.validarNome(dado,id.split('@')[2])

        return HttpResponse(validacao)
    
    if nome_validacao == "validar_nome_existente":

        id_item=id.split('@')[3]
        cpf=id.split('@')[2]

        validacao_nome=Validacoes.validarNomeExistente(id_item,dado)

        if validacao_nome != False:

            return HttpResponse(validacao_nome)
        
        validaca_cpf=Validacoes.validarCPFExistente(id_item,cpf)

        if validaca_cpf != False:

            return HttpResponse(validaca_cpf)

        return HttpResponse(False)
    
    if nome_validacao == "validar_mac_dispositivos":
        
        id_item=id.split('@')[2]

        validacao=Validacoes.validarMacDispositivos(id_item,dado)

        return HttpResponse(validacao)
    
    return HttpResponse("null")


def verificarAcesso(request):

    resposta=Validacoes.verificarAcesso()

    return HttpResponse(resposta)
    
     
