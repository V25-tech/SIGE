from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),

    path('alunos/', views.lista_alunos),

    path('emitir-declaracao/', views.emitir_declaracao),

    path('relatorio-pais/', views.relatorio_pais),

     path('admin/', admin.site.urls),
]

    