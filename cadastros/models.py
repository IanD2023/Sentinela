from django.db import models
from .radius.models import *
import time
# Create your models here.
class Cadastros(models.Model):
     
     nome = models.CharField(max_length=255,null=True)
     cpf = models.CharField(max_length=11,null=True)
     perfil = models.CharField(max_length=11,null=True)
     matricula = models.CharField(max_length=255,null=True)
     loja = models.IntegerField(null=True)
     setor = models.CharField(max_length=255,null=True)
     solicitante = models.CharField(max_length=255,null=True)
     usuario_criacao = models.CharField(max_length=255,null=True)
     qtd_dispositivos=models.IntegerField(null=True)
     tempo_acesso=models.CharField(max_length=255,null=True)
     data_criacao=models.DateField()
     data_modificacao=models.DateField()
     
     class Meta:
        
        db_table = 'cadastros'

     def __str__(self):

          self.nome
          self.cpf
          self.matricula
          self.tempo_acesso

          return self



class MACs(models.Model):
     
     nome = models.CharField(max_length=255,null=True)
     cpf = models.CharField(max_length=11,null=True)
     mac = models.CharField(max_length=17,null=True)
     matricula = models.CharField(max_length=255,null=True)
     loja = models.IntegerField(null=True)
     setor = models.CharField(max_length=255,null=True)
     usuario_criacao = models.CharField(max_length=255,null=True)
     tipo = models.IntegerField(null=True)
     seq = models.IntegerField(null=True)
     cod_dispositivo = models.IntegerField(null=True)

     
     class Meta:
        
        db_table = 'mac_addresses'
     
     def __str__(self):
         
          str(self.nome)
          str(self.mac)
          str(self.cpf)
          str(self.matricula)
          str(self.setor)
          str(self.tipo)


          return self


class Perfil(models.Model):

    codigo=models.IntegerField()
    nome= models.CharField(max_length=255,null=True)

    class Meta:
        
        db_table = 'perfil'

    def __str__(self):

          
          self.nome

          return self
     
         


