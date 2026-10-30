from django.contrib import admin

from .models import (
    Nota,
    PlanoAula,
    ReuniaoHTPC,
    ReuniaoPais,
    IndicadorPedagogico,
    PlanoMelhoria
)

admin.site.register(Nota)
admin.site.register(PlanoAula)
admin.site.register(ReuniaoHTPC)
admin.site.register(ReuniaoPais)
admin.site.register(IndicadorPedagogico)
admin.site.register(PlanoMelhoria)