from django.contrib import admin

from .models import (
    Nota,
    PlanoAula,
    ReuniaoHTPC,
    ReuniaoPais,
    IndicadorPedagogico,
    PlanoMelhoria,
    HistoricoEscolar,
    ParecerProfessor,
    RelatorioSemestral,
    Entrega,
)

admin.site.register(Nota)
admin.site.register(PlanoAula)
admin.site.register(ReuniaoHTPC)
admin.site.register(ReuniaoPais)
admin.site.register(IndicadorPedagogico)
admin.site.register(PlanoMelhoria)
admin.site.register(HistoricoEscolar)
admin.site.register(ParecerProfessor)
admin.site.register(RelatorioSemestral)
admin.site.register(Entrega)