from ..models import RADCHECK as radcheck ,RADREPLY as radreply


class RADCHECK:

    def __init__(self):
         pass
     
    def buscarID(id):

        try:

            mac=radcheck.objects.get(id=id)

            return mac
        
        except: return False
    
    def buscarMac(mac):

        ids_macs=[]
        
        try:

            for x in mac:
                
                try:

                    macs=radcheck.objects.get(username=x.mac)

                    if macs.id:
                    
                        macsadd={}
                        macsadd['id']=macs.id
                        macsadd['mac']=macs.username
                        ids_macs.append(macsadd)
                        macsadd={}
                
                except:
                
                    print("mac não encontrado")

            return ids_macs
        
        except:

            return False

    def editar(id,mac,codigo,perfil):

        from dispositivos.controller.dispositivosController import Dispositivos
        
        vlan=Dispositivos.buscaCodigo(codigo)
        print(perfil)
        if perfil == '2': 
            print("perfil")
            vlan.vlan=98

        try:

            if RADREPLY.editar(id,mac,vlan.vlan) == True:

                registro=radcheck.objects.get(id=id)

                registro.username=mac
                registro.value=mac
                registro.save() 

        except:  

            return False          



    def excluirMac(id):

        try:

            mac=radcheck.objects.get(id=id)
            mac.delete()

        except: print("erro")      



class RADREPLY:

    def __init__(self):
         pass
     
    def buscarID(id):

        mac=radreply.objects.get(id=id)


        return mac
    
    def buscarMac(mac):

        ids_macs=[]

        try:

            for x in mac:

                try:

                    macs=radreply.objects.filter(username=x)

                    for i in macs:

                        if i.id:
                        
                            macsadd={}
                            macsadd['id']=i.id
                            macsadd['mac']=i.username
                            ids_macs.append(macsadd)
                            macsadd={}
                
                except:
                
                    print("mac não encontrado")

            return ids_macs
        
        except:

            return False


    def editar(id,mac,vlan):
        

        mac_radcheck=RADCHECK.buscarID(id)  

        if  mac_radcheck != False:     

            registros=radreply.objects.filter(username=mac_radcheck.username)

            for x in registros:

                x.username=mac

                if x.attribute == 'Tunnel-Private-Group-ID':
                    
                    x.value=vlan

                x.save()

            return True     

    def excluirMac(id):
        
        try:
            mac=RADCHECK.buscarID(id)

            macs=radreply.objects.filter(username=mac.username)

            for x in macs:

                x.delete()
        except: print("erro")         
                    