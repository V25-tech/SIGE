from django.db import models


class Documento(models.Model):

    aluno = models.ForeignKey(
        'alunos.Aluno',
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

        return self.tipo_documento


class ModeloDeclaracao(models.Model):

    nome = models.CharField(
        max_length=100
    )

    texto = models.TextField()

    ativo = models.BooleanField(
        default=True
    )

    class Meta:

        verbose_name = 'Modelo de Declaração'

        verbose_name_plural = 'Modelos de Declaração'

    def __str__(self):

        return self.nome