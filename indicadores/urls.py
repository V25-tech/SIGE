from django.urls import path

from .views import (
    dashboard_direcao,
    importar_planilha,
    historico_apm,
)

urlpatterns = [

    path(
        '',
        dashboard_direcao,
        name='dashboard'
    ),

    path(
        'importar-planilha/',
        importar_planilha,
        name='importar_planilha'
    ),

    path(
        'historico-apm/',
        historico_apm,
        name='historico_apm'
    ),

]