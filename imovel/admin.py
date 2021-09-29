from django.contrib import admin
from .models import Imovel

@admin.register(Imovel)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('descricao','endereco','valor_imovel','data_inclusao','tipo','status')
    
