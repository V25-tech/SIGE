from django.db import models
from alunos.models import Aluno


class Documento(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    tipo_documento = models.CharField(
        max_length=50
    )

    data_emissao = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return f"{self.tipo_documento} - {self.aluno.nome}"