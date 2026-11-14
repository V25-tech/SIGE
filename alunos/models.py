from django.db import models


class Responsavel(models.Model):

    nome = models.CharField(
        max_length=200
    )

    cpf = models.CharField(
        max_length=14,
        unique=True
    )

    telefone = models.CharField(
        max_length=20
    )

    whatsapp = models.CharField(
        max_length=20,
        blank=True
    )

    class Meta:

        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

    def __str__(self):

        return self.nome


class Aluno(models.Model):

    nome = models.CharField(
        max_length=200
    )

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


class BuscaAtiva(models.Model):

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    data_registro = models.DateField(
        auto_now_add=True
    )

    quantidade_faltas = models.IntegerField()

    motivo_faltas = models.TextField()

    possui_atestado = models.BooleanField(
        default=False
    )

    responsavel_contato = models.CharField(
        max_length=200
    )

    telefone_contato = models.CharField(
        max_length=20
    )

    contato_telefonico = models.BooleanField(
        default=False
    )

    visita_domiciliar = models.BooleanField(
        default=False
    )

    professor_responsavel = models.CharField(
        max_length=100
    )

    observacoes = models.TextField(
        blank=True
    )

    class Meta:

        verbose_name = 'Busca Ativa'
        verbose_name_plural = 'Buscas Ativas'

    def __str__(self):

        return (
            f"{self.aluno.nome} - "
            f"{self.quantidade_faltas} faltas"
        )


class HistoricoContato(models.Model):

    busca_ativa = models.ForeignKey(
        BuscaAtiva,
        on_delete=models.CASCADE,
        related_name='historicos'
    )

    data_contato = models.DateField()

    tipo_contato = models.CharField(
        max_length=100
    )

    responsavel_falou = models.CharField(
        max_length=200,
        blank=True
    )

    observacoes = models.TextField(
        blank=True
    )

    class Meta:

        verbose_name = 'Histórico de Contato'
        verbose_name_plural = 'Históricos de Contato'

    def __str__(self):

        return (
            f"{self.data_contato} - "
            f"{self.tipo_contato}"
        )