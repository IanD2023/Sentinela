from django.urls import path
from django.conf import settings
from django.template.response import TemplateResponse 
from .views import login,home,editar,criar,funcionario,visitante,criarFuncionario,criarVisitante,excluirCadastro,ajustes,buscarColaborador
from .views import listarUsuarios,editarUsuario,criarUsuario,verificacoes,excluirUsuario,alterarSenha,verificarAcesso

urlpatterns = [

    path('', login,name="login"),
    path('home/', home,name="home"),
    path('editar/<int:id>', editar,name="editar"),
    path('criar/', criar,name="criar"),
    path('funcionario/', funcionario,name="funcionario"),
    path('visitante/', visitante,name="visitante"),
    path('ajustes/', ajustes,name="ajustes"),
    path('criar_funcionario/', criarFuncionario,name="criarFuncionario"),
    path('criar_visitante/', criarVisitante,name="criarVisitante"),
    path('funcionario/excluir/<int:id>', excluirCadastro,name="excluirCadastro"),
    path('visitante/excluir/<int:id>', excluirCadastro,name="excluirCadastro"),
    path('buscarColaborador/<int:id>', buscarColaborador,name="buscarColaborador"),
    path('usuarios/', listarUsuarios,name="listarUsuarios"),
    path('usuarios/criar/', criarUsuario,name="criarUsuario"),
    path('usuarios/editar/<int:id>', editarUsuario,name="editarUsuario"),
    path('usuarios/excluir/<int:id>', excluirUsuario,name="excluirUsuario"),
    path('alterarsenha/<int:id>', alterarSenha,name="alterarSenha"),
    path('verificacoes/<str:id>', verificacoes,name="verificacoes"),
    path('verificaracesso/', verificarAcesso,name="verificarAcesso"),

]