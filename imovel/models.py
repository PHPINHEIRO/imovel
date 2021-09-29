from django.db import models

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)
    
    def get_by_id(self, id):
        return self.filter(id=id).get()


class Imovel(models.Model):
    STATUS = [
        (True,'Ativo'),
        (False,'Inativo')
    ]

    TIPO = [
        ('APARTAMENTO','Apartamento'),
        ('LOTE','Lote')
    ]

    descricao = models.CharField(verbose_name='Descrição', max_length=255)
    endereco = models.CharField(verbose_name='Endereço',max_length=255)
    valor_imovel = models.DecimalField(verbose_name='Valor do Imovel', max_digits=10, decimal_places=2)
    data_inclusao = models.DateField(verbose_name='Data Cadastro', auto_now_add=True)
    tipo = models.CharField(verbose_name='Tipo', max_length=11, choices=TIPO)
    status = models.BooleanField(verbose_name='Status', choices=STATUS)
    
    objects = models.Manager()
    available = AvailableManager()

    class Meta():
        ordering = ('descricao','valor_imovel',)

    def __str__(self) -> str:
        return self.descricao

    @property
    def comissao(self):
        return float(self.valor_imovel) * 0.05
    

