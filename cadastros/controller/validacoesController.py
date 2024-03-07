from ..models import Cadastros as cadastros,MACs as macs,Perfil,RADCHECK as radcheck, RADREPLY as radreply
from cadastros.models import MACs
from cadastros.models import Cadastros
from .cadastrosController import Cadastros as CadastrosController
from .macsController import MACs as macs
from datetime import datetime ,timedelta

class Validacoes:

    def __init__(self,nome_validacao,valor):
            
        self.nome_validacao=nome_validacao
        self.valor=valor

    def validarMac(mac):
        
        try:

            print(mac)

            MACs.objects.get(mac=mac)
            msg="Endereço mac já cadastrado"
            return msg
        
        except:

            print("mac não encontrado")

            return False  

    def validarMacExistente(mac,nome):
         
        try:

            MACs.objects.get(mac=mac,nome=nome)
            msg=("Endereço mac já cadastrado para este usuário")
            
            return False
        
        except:

            try:

                MACs.objects.get(mac=mac)
                msg="Endereço mac já cadastrado"
                return msg
            
            except:

                return False

    def validarMacDispositivos(id,mac):
         
        try:

            MACs.objects.get(id=id,mac=mac)
            msg=("Endereço mac já cadastrado para este usuário")
            
            return False
        
        except:

            try:

                MACs.objects.get(mac=mac)
                msg="Endereço mac já cadastrado"
                return msg
            
            except:

                return False        

    def validarNome(nome,cpf):

        print(nome)

         
        try:

            cadastro=Cadastros.objects.get(nome=nome)

            if cadastro.perfil == 1: msg=("Nome já cadastrado como Funcionário")
            else: msg=("Nome já cadastrado como Visitante")

            
            return msg
        
        except:

            try:

                cadastro=Cadastros.objects.get(cpf=cpf)

                if cadastro.perfil == 1: msg=("CPF já cadastrado como Funcionário")
                else: msg=("CPF já cadastrado como Visitante")
            
                return msg
            
            except:
                return False 

    def validarNomeExistente(id,nome):

        try:

            Cadastros.objects.get(id=id,nome=nome)

            return False

        except:

            try:

                Cadastros.objects.get(nome=nome)

                msg=("Nome já cadastrado")

                return msg
            
            except:

                return False

    def validarCPFExistente(id,cpf):

        try:

            Cadastros.objects.get(id=id,cpf=cpf)

            return False

        except:

            try:

                Cadastros.objects.get(cpf=cpf)

                msg=("CPF já cadastrado")

                return msg     
            
            except:

                return False

    def verificarAcesso():
     
        visitantes=CadastrosController().listarVisitante()

        for x in visitantes:

            data_expiracao=x.data_modificacao + timedelta(int(x.tempo_acesso))

            if data_expiracao < datetime.today():

                listademacs=macs(x.nome,x.cpf,x.matricula).dispositivos()

                for i in listademacs:

                    if i != "":

                        try:  

                            radcheck.objects.get(username=i.mac).delete()

                            radreply.objects.filter(username=i.mac).delete()   
                                
                        except:    
                                return False

                        i.delete()

                x.tempo_acesso = 1
                x.data_modificacao = datetime.today()
                x.save()       

        return True                

                        
               




