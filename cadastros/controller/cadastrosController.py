from ..models import Cadastros as cadastros,MACs as macs,Perfil,RADCHECK as radcheck, RADREPLY as radreply
from .macsController import MACs
from django.db.models import Count
from datetime import datetime

class Cadastros:

 def __init__(self):
    pass

 def listarCadastros(self):
     
     try: 
   
         macs=cadastros.objects.all().order_by('nome')

         return macs
     
     except:

        return False
     
 def listarFuncionarios(self):
     
     funcionarios=cadastros.objects.filter(perfil=1)

     return funcionarios
 
 def listarFuncionarioFiltro(self,nome, matricula,mac,loja):

    funcionarios=cadastros.objects.filter(perfil=1).order_by('nome')

    if nome:
        funcionarios=cadastros.objects.filter(perfil=1, nome__icontains=nome).order_by('nome')
    if matricula:
        funcionarios=cadastros.objects.filter(perfil=1, matricula=matricula).order_by('nome')
    if mac:
        try:    
            dados_mac=macs.objects.get(mac=mac)
            funcionarios=cadastros.objects.filter(perfil=1, nome=dados_mac.nome,matricula=dados_mac.matricula).order_by('nome')
        except: 
            funcionarios=cadastros.objects.filter(perfil=3).order_by('nome')
    if loja:
        funcionarios=cadastros.objects.filter(perfil=1, loja=loja).order_by('nome')

    return funcionarios
     
 def listarVisitante(self):
     
     funcionarios=cadastros.objects.filter(perfil=2)

     return funcionarios
 
 def listarVisitanteFiltro(self, nome, mac, cpf):
     
    funcionarios=cadastros.objects.filter(perfil=2).order_by('nome')

    if nome:
        funcionarios=cadastros.objects.filter(perfil=2, nome__icontains=nome).order_by('nome')
    if mac:        
        try:
            macsFuncionario = macs.objects.get(mac=mac)   
            #print(macsFuncionario[0])
            funcionarios=cadastros.objects.filter(perfil=2, nome__icontains=macsFuncionario.nome).order_by('nome') 
       
        except:
            funcionarios=cadastros.objects.filter(perfil=3).order_by('nome')
    if cpf:
        funcionarios=cadastros.objects.filter(perfil=2, cpf__icontains=cpf).order_by('nome') 

    return funcionarios
        
     
 def buscaId(self,id):

    try:
   
        cadastro=cadastros.objects.get(id=id)

        return cadastro
     
    except:

        return False

 def buscaMatricula(self,matricula):

    try:
   
        cadastro=cadastros.objects.get(matricula=matricula)

        return cadastro
     
    except:

        return False  
    
 def perfil(self):
     
     perfis=Perfil.objects.all()

     return perfis

 def criarcadastro(self,nome,perfil,cpf,matricula,tempo_acesso,loja,setor,usuario_criacao):
     
      try: 
         cadastros.objects.get(nome=nome)
         msg = "Nome já Cadastrado"
         return msg
      except:   
         pass
      
      try: 
         cadastros.objects.get(cpf=cpf)
         msg = "CPF já Cadastrado"
         return msg
      except:
            pass
      try: 
         cadastros.objects.get(matricula=nome)
         msg = "Matrícula já Cadastrado"
         return msg
      except:
         pass
      
      if perfil == '2': 
        solicitante=setor
        setor=""
      else: 
          solicitante=""

      cadastros.objects.create(nome=nome,perfil=perfil,cpf=cpf,matricula=matricula,data_criacao=datetime.now(),data_modificacao=datetime.now(),tempo_acesso=tempo_acesso,loja=loja,setor=setor,solicitante=solicitante,usuario_criacao=usuario_criacao)  
     
      return True
 
 def editar(self,id,nome,perfil,cpf,mac,matricula,tipo,loja,setor,tempo_acesso,solicitante,usuario_criacao):

        cadastro=cadastros.objects.get(id=id)
        cadastro.nome=nome
        cadastro.perfil=perfil
        cadastro.cpf=cpf
        cadastro.mac=mac
        cadastro.matricula=matricula
        cadastro.loja=loja
        cadastro.setor=setor
        cadastro.tipo=tipo
        cadastro.solicitante =solicitante
        cadastro.usuario_criacao=usuario_criacao
        if cadastro.perfil == '1':
            cadastro.tempo_acesso=100
        else:    
            cadastro.tempo_acesso=tempo_acesso
            cadastro.data_modificacao=datetime.today()

        cadastro.save()

 def excluir(self,id):
     
     try:
     
      cadastro=cadastros.objects.get(id=id)

      macs=MACs(cadastro.nome,cadastro.cpf,cadastro.matricula).dispositivos()

      for x in macs:
        
        try:  

            radcheck.objects.get(username=x.mac).delete()

            radreply.objects.filter(username=x.mac).delete()   
                 
        except:    
                return False

        x.delete()

      cadastro.delete()    

     except: False 

    

          


    




   


