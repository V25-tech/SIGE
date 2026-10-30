from django.db import models


class Responsavel(models.Model):

    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

    def __str__(self):
        return self.nome


class Aluno(models.Model):

    nome = models.CharField(max_length=200)

    matricula = models.CharField(
        max_length=20,
        unique=True
    )

    data_nascimento = models.DateField()

    turma = models.CharField(
        max_length=100
    )

    responsavel = models.ForeignKey(
        Responsavel,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome