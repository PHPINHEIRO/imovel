from django.db import models

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)
    
    def get_by_id(self, id):
        return self.filter(id=id).get()

class Cliente(models.Model):

    STATUS = [
        (True,'Ativo'),
        (False,'Inativo')
    ]

    nome = models.CharField(name='nome',verbose_name='Nome',max_length=255)
    email = models.EmailField(name='email',verbose_name='Email',unique=True,db_index=True,max_length=255)
    cpf = models.CharField(name='cpf',verbose_name='CPF',unique=True,db_index=True,max_length=14)
    telefone = models.CharField(name='telefone',verbose_name='Telefone',max_length=15)
    dtainclusao = models.DateField(name='dtainclusao',verbose_name='Data Cadastro',auto_now_add=True)
    status = models.BooleanField(name='status',verbose_name='Status',choices=STATUS) 

    available = AvailableManager()
    
    class Meta():
        ordering = ('nome','dtainclusao',)

    def __str__(self) -> str:
        return self.nome