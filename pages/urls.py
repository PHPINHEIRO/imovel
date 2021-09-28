from django.urls import path

from .views import HomePageView,VendaPageView, RelatorioPageView

app_name = 'pages'

urlpatterns = [
    path("",HomePageView.as_view(),name='home'),
    path("venda/",VendaPageView.as_view(),name='venda'),
    path("relatorio/",RelatorioPageView.as_view(),name='relatorio')
]