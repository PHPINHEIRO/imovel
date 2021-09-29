from django.urls import path

from .views import HomePageView,VendaPageView, RelatorioPageView

app_name = 'pages'

urlpatterns = [
    path("imoveis",HomePageView.as_view(), name='imoveis'),
    path("venda/<int:id_imovel>",VendaPageView.as_view(), name='venda'),
    path("relatorio/<int:id_venda>",RelatorioPageView.as_view(), name='relatorio')
]