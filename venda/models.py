from django.db import models
from cliente.models import Cliente
from vendedor.models import Vendedor
from imovel.models import Imovel

class Venda(models.Model):

    CONDPAGTO = [
        (1,'Avista'),
        (180,'180x')
    ]


    imovel = models.ForeignKey(to=Imovel,on_delete=models.DO_NOTHING,name='imovel',verbose_name='Imovel',blank=False,null=False)
    vendedor =  models.ForeignKey(to=Vendedor,on_delete=models.DO_NOTHING, name='vendedor',verbose_name='Vendedor',blank=False,null=False)
    cliente =  models.ForeignKey(to=Cliente,on_delete=models.DO_NOTHING, name='cliente',verbose_name='Cliente',blank=False,null=False)
    dtainclusao = models.DateField(name='dtainclusao',verbose_name='Data Cadastro',auto_now_add=True)
    condpagto = models.IntegerField(name='condpagto',verbose_name='Condicoes de Pagamento',default=1,choices=CONDPAGTO)
    
    class Meta():
        ordering = ('vendedor','dtainclusao',)

    def __str__(self) -> str:
        return str(self.id)



