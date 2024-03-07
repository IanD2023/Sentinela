from django.urls import path
from django.conf import settings
from django.template.response import TemplateResponse 
from .views import editarDispositivo,dispositivos,criarDispositivo
from .Views.coletorView import  coletores,criarColetor,editarColetor,excluirColetor
from .Views.balancaView import balanca,criarBalanca,editarBalanca,excluirBalanca

urlpatterns = [    
    path('', coletores,name="coletores"),
    path('criar/', criarDispositivo,name="criarDispositivo"),
    path('editar/<int:id>', editarDispositivo,name="editarDispositivo"),
    path('coletores/', coletores,name="coletores"),
    path('coletores/criar_coletor/', criarColetor,name="criarColetor"),
    path('coletores/editar/<int:id>', editarColetor,name="editarColetor"),
    path('coletores/excluir/<int:id>', excluirColetor,name="excluirColetor"),
    path('balanca/', balanca,name="balanca"),
    path('balanca/criar/', criarBalanca,name="criarBalanca"),
    path('balanca/editar/<int:id>', editarBalanca,name="editarBalanca"),
    path('balanca/excluir/<int:id>', excluirBalanca,name="excluirBalanca"),
]