from django.db import models

class Imovel(models.Model):
    STATUS = [
        (True,'Ativo'),
        (False,'Inativo')
    ]

    TIPO = [
        ('APARTAMENTO','Apartamento'),
        ('LOTE','Lote')
    ]

    descricao = models.CharField(name='descricao',verbose_name='Descricao',unique=True,max_length=255)
    endereco = models.CharField(name='endereco',verbose_name='Endereco',max_length=255)
    vlrimovel = models.DecimalField(name='vlrimovel',verbose_name='Valor Imovel',max_digits=10,decimal_places=2)
    vlrcomissao = models.DecimalField(name='vlrcomissao',verbose_name='Valor Comissao(%)',max_digits=5,decimal_places=2)
    dtainclusao = models.DateField(name='dtainclusao',verbose_name='Data Cadastro',auto_now_add=True) 
    tipo = models.CharField(name='tipo',verbose_name='Tipo',max_length=11,choices=TIPO)
    status = models.BooleanField(name='status',verbose_name='Status',choices=STATUS)
    
    class Meta():
        ordering = ('descricao','vlrimovel',)

    def __str__(self) -> str:
        return self.descricao
