from django.contrib import admin

from .models import (
    Responsavel,
    Aluno,
    BuscaAtiva,
    HistoricoContato
)

admin.site.register(Responsavel)
admin.site.register(Aluno)
admin.site.register(BuscaAtiva)
admin.site.register(HistoricoContato)