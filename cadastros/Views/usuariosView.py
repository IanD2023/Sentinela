from cadastros.controller.usuariosController import Usuarios
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def listarUsuarios(request):
 
    usuarios=Usuarios.listarUsuarios()

    for list in usuarios:
        list.date_joined=list.date_joined.strftime("%d/%m/%Y")

    return render(request,'usuarios/index.html',{'usuarios':usuarios})

@user_passes_test(lambda u: u.is_superuser)
def criarUsuario(request):

    nome=request.POST.get('nome')
    login=request.POST.get('login')
    senha=request.POST.get('senha')
    perfil=request.POST.get('perfil')

    if nome:

        if Usuarios(nome,senha,login,perfil).criar() == True:
 
            return redirect(listarUsuarios)
    
    return render(request,'usuarios/criar.html')

@user_passes_test(lambda u: u.is_superuser)
def editarUsuario(request,id):

    nome=request.POST.get('nome')
    login=request.POST.get('login')
    senha=request.POST.get('senha')
    perfil=request.POST.get('perfil')
    usuario=Usuarios.BuscaId(id)

    if nome:

        if Usuarios(nome,senha,login,perfil).editar(id) == True:

            return redirect(listarUsuarios)
    
    return render(request,'usuarios/editar.html',{'usuario':usuario})

@user_passes_test(lambda u: u.is_superuser)
def excluirUsuario(request,id):

    excluir=request.POST.get("excluir")
    usuario=Usuarios.BuscaId(id)

    if excluir:

        if Usuarios.excluir(id) == True:

            return redirect(listarUsuarios)
    
    return render(request,'usuarios/excluir.html',{'usuario':usuario})

@login_required
def alterarSenha(request,id):

    novaSenha=request.POST.get("novasenha")
    usuario=Usuarios.BuscaId(id)

    if novaSenha:

        if Usuarios(usuario.first_name,novaSenha,usuario.username,usuario.is_superuser).alterarSenha(id) == True:

            return redirect('/')
    
    return render(request,'usuarios/alterarSenha.html',{'usuario':usuario})


