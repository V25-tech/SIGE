from django.urls import path

from .views import (
    alunos_home,
    busca_ativa,
    relatorio_conselho
)

urlpatterns = [

    path(
        '',
        alunos_home,
        name='alunos_home'
    ),

    path(
        'busca-ativa/',
        busca_ativa,
        name='busca_ativa'
    ),

    path(
    'conselho/<int:pk>/',
    relatorio_conselho,
    name='relatorio_conselho'
),

]