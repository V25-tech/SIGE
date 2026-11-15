from django.contrib import admin
from django.urls import path, include

from alunos.views import pagina_inicial

urlpatterns = [

    path(
        '',
        pagina_inicial,
        name='home'
    ),

    path(
        'alunos/',
        include('alunos.urls')
    ),

    path(
        'indicadores/',
        include('indicadores.urls')
    ),

    path(
        'admin/',
        admin.site.urls
    ),
]