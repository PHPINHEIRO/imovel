from django.views.generic import TemplateView, View
from django.shortcuts import HttpResponse, render, reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from imovel.models import Imovel
from cliente.models import Cliente
from venda.models import CONDICOES_PAGTO_CHOICES, Venda

from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/login/'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['imoveis'] = Imovel.available.all()
        return context

class VendaPageView(LoginRequiredMixin,View):
    login_url = '/admin/login/'
    template_name = 'venda.html'

    def get(self, request, id_imovel:int):
        
        try:
            imovel = Imovel.available.get_by_id(id_imovel)
        except Imovel.DoesNotExist as e:
            return HttpResponseNotFound('Imovel não encontrado')
        
        clientes = Cliente.available.all()

        return render(request, self.template_name, {
            'imovel': imovel,
            'condicoes_pagto': CONDICOES_PAGTO_CHOICES,
            'clientes': clientes
        })

    def post(self, request, id_imovel:int):

        id_cliente = request.POST.get('cliente_id')
        condicao_pagto = int(request.POST.get('condicao_pagto'))
        valor_imovel = float(request.POST.get('valor_imovel'))
        valor_comissao = float(request.POST.get('comissao'))

        if id_cliente is None:
            return HttpResponseNotFound('Voce precisa fornecer um cliente')

        try:
            imovel = Imovel.available.get_by_id(id_imovel)
        except Imovel.DoesNotExist as e:
            return HttpResponseNotFound('Imovel não encontrado')

        try:
            cliente = Cliente.available.get_by_id(int(id_cliente))
        except Cliente.DoesNotExist:
            return HttpResponseNotFound('Cliente não existe')

        venda = Venda()
        venda.imovel = imovel
        venda.cliente = cliente
        venda.vendedor = request.user
        venda.condicao_pagto = condicao_pagto
        venda.valor_imovel = valor_imovel
        venda.valor_comissao = valor_comissao
        venda.save()

        return HttpResponseRedirect(
            reverse('pages:relatorio', args=(venda.id, ))
        )


class RelatorioPageView(LoginRequiredMixin,View):
    login_url = '/admin/login/'
    template_name = 'relatorio.html'

    def get(self, request, id_venda:int):
        
        try:
            venda = Venda.objects.filter(id=id_venda).get()
        except Venda.DoesNotExist:
            return HttpResponseNotFound('Venda não encontrada')
        
        return render(request, self.template_name, {
            'venda': venda
        })
