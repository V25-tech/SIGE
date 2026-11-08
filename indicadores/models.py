from django.db import models


class AvaliacaoExterna(models.Model):

    avaliacao = models.CharField(
        max_length=100
    )

    data = models.DateField()

    turma = models.CharField(
        max_length=20
    )

    matriculados = models.IntegerField()

    participantes = models.IntegerField()

    faltosos = models.IntegerField()

    acima_meta = models.IntegerField()

    abaixo_meta = models.IntegerField()

    observacoes = models.TextField(
        blank=True
    )


class APM(models.Model):

    mes = models.IntegerField()

    ano = models.IntegerField()

    saldo_inicial = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    arrecadacao = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    despesas = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    observacao = models.TextField(
        blank=True
    )

    @property
    def saldo_final(self):

        return (
            self.saldo_inicial +
            self.arrecadacao -
            self.despesas
        )