from django.contrib import admin
from .models import Venda

@admin.register(Venda)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','vendedor','cliente','imovel','data_inclusao','condicao_pagto')