from django.contrib import admin
from .models import Aluno, Responsavel


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'matricula',
        'turma'
    )

    search_fields = (
        'nome',
        'matricula'
    )


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'cpf',
        'telefone'
    )

    search_fields = (
        'nome',
        'cpf'
    )