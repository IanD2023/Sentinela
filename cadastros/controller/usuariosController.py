from django.contrib.auth.models import User

class Usuarios:

    def __init__(self,nome,senha,login,perfil):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.perfil = perfil

    def listarUsuarios():

        try:

            usuarios = User.objects.all()
            return usuarios
        
        except:  

            return False
        
    def BuscaId(id):  

        try:
            usuario=User.objects.get(id=id)
            return usuario
        
        except:

            return False

    def criar(self):

        try:

            User.objects.create_user(username=self.login,first_name=self.nome,password=self.senha,is_superuser=self.perfil)
            return True
        
        except:

            return False

    def editar(self,id):

        try:

            usuario = User.objects.get(id=id)

            if self.senha != "**********":

                usuario.set_password(self.senha)

            usuario.first_name =self.nome
            usuario.username=self.login
            usuario.is_superuser=self.perfil
            usuario.save()

            return True
        
        except:  
            return False 

    def alterarSenha(self,id):

        try:

            usuario = User.objects.get(id=id)

            if self.senha != "**********":

                usuario.set_password(self.senha)
                
                usuario.save()

                return True
        
        except:  

            return False          

    def excluir(id):

        try:

            usuario = User.objects.get(id=id)

            usuario.delete()

            return True
        
        except:  
            return False     