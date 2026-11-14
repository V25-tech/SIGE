from django.contrib import admin

from .models import (
    Documento,
    ModeloDeclaracao
)

admin.site.register(Documento)
admin.site.register(ModeloDeclaracao)