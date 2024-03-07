from ..models import Cadastros as cadastros,MACs as macs,RADCHECK as radcheck, RADREPLY as radreply
from dispositivos.models import Dispositivos
from ..radius.controller.radiusController import RADCHECK as radcheckController, RADREPLY as radreplyController
from django.db.models import Count
from datetime import datetime

class MACs:

 def __init__(self,nome,cpf,matricula):
    self.nome=nome
    self.cpf=cpf
    self.matricula=matricula

 def buscaId(self,id):
     
     try:
     
      mac=macs.objects.get(id=id)
      
      return mac
     
     except: False


 def listarMacs(self):

    list=macs.objects.all()

    return list


 def criar(self,mac,tipo,seq,perfil):
     
      try: 

         macs.objects.get(mac=mac)
         msg = "Mac já Cadastrado"
         return msg
      
      except: pass

      vlan=Dispositivos.objects.get(codigo=tipo)
      if perfil == '2': vlan.vlan = 98
      macs.objects.create(nome=self.nome,cpf=self.cpf,matricula=self.matricula,mac=mac,tipo=tipo,seq=seq)

      ##if mac != "":

      radcheck.objects.create(username=mac,attribute='Cleartext-Password',op=':=',value=mac)
      radreply.objects.create(username=mac,attribute='Tunnel-Type',op='=',value='VLAN')
      radreply.objects.create(username=mac,attribute='Tunnel-Medium-Type',op='=',value='IEEE-802')
      radreply.objects.create(username=mac,attribute='Tunnel-Private-Group-ID',op='=',value=vlan.vlan)
     
      return True
 
 def editar(self,id,mac,tipo,seq,perfil):
    
         try:
            
            mac_dispositivo=macs.objects.get(id=id)
            mac_dispositivo.nome=self.nome
            mac_dispositivo.cpf=self.cpf
            mac_dispositivo.matricula=self.matricula
            mac_dispositivo.mac=mac
            mac_dispositivo.tipo=tipo
            mac_dispositivo.save()
      
         except:
         
            self.criar(mac,tipo,seq,perfil)

 def deletar(self,id):
    
      try: 

         mac_dispositivo=macs.objects.get(id=id)
         mac_dispositivo.delete()
     
      except:
          
          print("Mac não encontrado")
        
      #  return False      

 def dispositivos(self):

    qtd_cadastros=macs.objects.filter(nome=self.nome,cpf=self.cpf,matricula=self.matricula)

    return qtd_cadastros
 
 def listarDispositivo(self,tipo):
    
    listaDispositivos=macs.objects.filter(tipo=tipo)

    return listaDispositivos
 
 def listarDispositivoFiltro(self,tipo, loja, setor, mac):
    
   listaDispositivos=macs.objects.filter(tipo=tipo)

   if loja:
      listaDispositivos=macs.objects.filter(tipo=tipo, loja__icontains=loja)
   if setor:
      listaDispositivos=macs.objects.filter(tipo=tipo, setor__icontains=setor)
   if mac:
      listaDispositivos=macs.objects.filter(tipo=tipo, mac__icontains=mac)

   return listaDispositivos

    


    




   


