from ..models import Dispositivos as dispositivos
from cadastros.models import MACs,RADCHECK as radcheck, RADREPLY as radreply
from cadastros.radius.controller.radiusController import RADCHECK as radcheckController, RADREPLY as radreplyController
from cadastros.controller.macsController import MACs as macs


class Dispositivos:

    def __init__(self,nome,vlan):
        
        self.nome=nome
        self.vlan=vlan

    def listar(self):

        lista_dispositivos=dispositivos.objects.all()

        return lista_dispositivos
    
    def buscaId(self,id):

        device=dispositivos.objects.get(id=id)

        return device
    
    def buscaCodigo(codigo):

        print(codigo)

        device=dispositivos.objects.get(codigo=codigo)

        return device
    
    def buscaIdColetor(self,id):

        device=MACs.objects.get(id=id)

        return device

    def criar(self):

        try:

            dispositivos.objects.create(nome=self.nome,vlan=self.vlan)

        except:

            return False


    def editar(self,id):

        try:

            device=dispositivos.objects.get(id=id)
            device.nome=self.nome
            device.vlan=self.vlan
            device.save()

        except:

            return False

    def criarColetor(self,mac,loja,setor,usuario_criacao):

      try: 

         MACs.objects.get(mac=mac)
         msg = "Mac já Cadastrado"
         return msg
      
      except: pass
     
      MACs.objects.create(mac=mac,nome="COLETOR",loja=loja,setor=setor,tipo=3,cod_dispositivo=3,usuario_criacao=usuario_criacao)
      radcheck.objects.create(username=mac,attribute='Cleartext-Password',op=':=',value=mac)
      radreply.objects.create(username=mac,attribute='Tunnel-Type',op='=',value='VLAN')
      radreply.objects.create(username=mac,attribute='Tunnel-Medium-Type',op='=',value='IEEE-802')
      radreply.objects.create(username=mac,attribute='Tunnel-Private-Group-ID',op='=',value=27)
     
      return True
 
    def editarColetor(self,id,loja,setor,numero_mac,vlan,usuario_criacao):

     # try:

         mac=MACs.objects.filter(id=id)

         id_rad_check=radcheckController.buscarMac(mac)

         for x in id_rad_check:

            radcheckController.editar(x['id'],numero_mac,vlan,"")

         for i in mac:
             
            i.loja=loja
            i.setor=setor
            i.mac= numero_mac
            i.usuario_criacao=usuario_criacao
            i.save()    

    def excluirColetor(self,id):
     
     try:
     
        cadastro=MACs.objects.filter(id=id)
        mac=radcheckController.buscarMac(cadastro)
        for x in mac:

            radreplyController.excluirMac(x['id'])
            radcheckController.excluirMac(x['id'])

        cadastro.delete()    

     except: False

    def listarBalancas(self):

        balancas=MACs.objects.filter(cod_dispositivo=10)

        return balancas
    

    def listarBalancasFiltro(self,loja,setor,mac):

        balancas=MACs.objects.filter(cod_dispositivo=10)

        if loja:
            balancas=MACs.objects.filter(cod_dispositivo=10, loja__icontains=loja)
        if setor:
            balancas=MACs.objects.filter(cod_dispositivo=10, setor__icontains=setor)
        if mac:
            balancas=MACs.objects.filter(cod_dispositivo=10, mac__icontains=mac)

        return balancas        


    def criarBalanca(self,mac,loja,setor,usuario_criacao):

      try: 

         MACs.objects.get(mac=mac)
         msg = "Mac já Cadastrado"

         return msg
      
      except: pass

      print("criando balanca")
     
      MACs.objects.create(mac=mac,nome="BALANCA",loja=loja,setor=setor,tipo=10,cod_dispositivo=10,usuario_criacao=usuario_criacao)
      radcheck.objects.create(username=mac,attribute='Cleartext-Password',op=':=',value=mac)
      radreply.objects.create(username=mac,attribute='Tunnel-Type',op='=',value='VLAN')
      radreply.objects.create(username=mac,attribute='Tunnel-Medium-Type',op='=',value='IEEE-802')
      radreply.objects.create(username=mac,attribute='Tunnel-Private-Group-ID',op='=',value=22)
     
     
      return True           