from django.db import models

# Create your models here.
class Dispositivos(models.Model):

    codigo=models.IntegerField(null=True)
    nome= models.CharField(max_length=255,null=True)
    vlan=models.IntegerField()

    class Meta:
        
        db_table = 'dispositivos'

    def __str__(self):
          
          self.nome

          return self  