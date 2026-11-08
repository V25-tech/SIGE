from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [

    path(
        '',
        views.home
    ),

    path(
        'indicadores/',
        include('indicadores.urls')
    ),

    path(
        'emitir-declaracao/',
        views.emitir_declaracao
    ),

    path(
        'relatorio-pais/',
        views.relatorio_pais
    ),

    path(
        'admin/',
        admin.site.urls
    ),

]