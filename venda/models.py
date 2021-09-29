from django.db import models


CONDICOES_PAGTO_CHOICES = [
    (1, 'À vista'),
    (180, '180x')    
]


class Venda(models.Model):

    imovel = models.ForeignKey('imovel.Imovel', on_delete=models.SET_NULL, verbose_name='Imovel', blank=False, null=True, related_name='vendas')
    vendedor =  models.ForeignKey('vendedor.Vendedor',on_delete=models.SET_NULL,verbose_name='Vendedor',blank=False,null=True, related_name='vendas')
    cliente =  models.ForeignKey('cliente.Cliente',on_delete=models.SET_NULL,verbose_name='Cliente',blank=False,null=True, related_name='vendas')
    data_inclusao = models.DateField(verbose_name='Data Cadastro',auto_now_add=True)
    condicao_pagto = models.IntegerField(verbose_name='Condicoes de Pagamento',default=1,choices=CONDICOES_PAGTO_CHOICES)
    valor_imovel = models.DecimalField(verbose_name='Valor do Imovel',max_digits=10, decimal_places=2)
    valor_comissao = models.DecimalField(verbose_name='Comissao', max_digits=10, decimal_places=2)
    
    class Meta():
        ordering = ('vendedor','data_inclusao',)

    def __str__(self) -> str:
        return str(self.id)



