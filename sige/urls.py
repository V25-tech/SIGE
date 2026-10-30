from django.contrib import admin
from django.urls import path

from .views import home
from .views import lista_alunos
from .views import emitir_declaracao

urlpatterns = [
    path('', home),
    path('alunos/', lista_alunos),
    path('emitir-declaracao/', emitir_declaracao),
    path('admin/', admin.site.urls),
]