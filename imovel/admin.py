from django.contrib import admin
from .models import Imovel

@admin.register(Imovel)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('descricao','endereco','vlrimovel','vlrcomissao','dtainclusao','tipo','status')
    
