from django.db import models
from alunos.models import Aluno, Responsavel

class Entrega(models.Model):

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    responsavel = models.ForeignKey(
        Responsavel,
        on_delete=models.CASCADE
    )

    tipo = models.CharField(
        max_length=100
    )

    data_entrega = models.DateField()

    observacoes = models.TextField()

    class Meta:
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"

    def __str__(self):
        return f"{self.aluno.nome} - {self.tipo}"

class Nota(models.Model):

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    disciplina = models.CharField(max_length=100)

    nota = models.DecimalField(
        max_digits=4,
        decimal_places=1
    )

    bimestre = models.IntegerField()

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"

    def __str__(self):
        return f"{self.aluno.nome} - {self.disciplina}"


class PlanoAula(models.Model):

    professor = models.CharField(max_length=200)

    disciplina = models.CharField(max_length=100)

    turma = models.CharField(max_length=50)

    objetivo = models.TextField()

    metodologia = models.TextField()

    recursos = models.TextField()

    data_aula = models.DateField()

    class Meta:
        verbose_name = "Plano de Aula"
        verbose_name_plural = "Planos de Aula"

    def __str__(self):
        return self.disciplina


class ReuniaoHTPC(models.Model):

    data = models.DateField()

    pauta = models.TextField()

    decisoes = models.TextField()

    class Meta:
        verbose_name = "Reunião HTPC"
        verbose_name_plural = "Reuniões HTPC"

    def __str__(self):
        return f"HTPC {self.data}"


class ReuniaoPais(models.Model):

    data = models.DateField()

    turma = models.CharField(max_length=50)

    pauta = models.TextField()

    encaminhamentos = models.TextField()

    class Meta:
        verbose_name = "Reunião com Pais"
        verbose_name_plural = "Reuniões com Pais"

    def __str__(self):
        return f"Reunião {self.turma}"


class IndicadorPedagogico(models.Model):

    ano_escolar = models.CharField(max_length=30)

    componente = models.CharField(max_length=100)

    meta_mec = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    resultado = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    observacoes = models.TextField()

    class Meta:
        verbose_name = "Indicador Pedagógico"
        verbose_name_plural = "Indicadores Pedagógicos"

    def __str__(self):
        return self.componente

class PlanoMelhoria(models.Model):

    indicador = models.ForeignKey(
        IndicadorPedagogico,
        on_delete=models.CASCADE
    )

    acao = models.TextField()

    responsavel = models.CharField(
        max_length=200
    )

    prazo = models.DateField()

    class Meta:
        verbose_name = "Plano de Melhoria"
        verbose_name_plural = "Planos de Melhoria"

    def __str__(self):
        return self.responsavel


class HistoricoEscolar(models.Model):

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    ano_letivo = models.IntegerField()

    turma = models.CharField(
        max_length=50
    )

    resultado_final = models.CharField(
        max_length=50
    )

    observacoes = models.TextField()

    class Meta:
        verbose_name = "Histórico Escolar"
        verbose_name_plural = "Históricos Escolares"

    def __str__(self):
        return f"{self.aluno.nome} - {self.ano_letivo}"


class ParecerProfessor(models.Model):

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    professor = models.CharField(
        max_length=200
    )

    semestre = models.CharField(
        max_length=20
    )

    parecer = models.TextField()

    pontos_melhorar = models.TextField()

    data = models.DateField()

    class Meta:
        verbose_name = "Parecer do Professor"
        verbose_name_plural = "Pareceres dos Professores"

    def __str__(self):
        return f"{self.aluno.nome} - {self.professor}"


class RelatorioSemestral(models.Model):

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    semestre = models.CharField(
        max_length=20
    )

    faltas = models.IntegerField()

    observacoes = models.TextField()

    class Meta:
        verbose_name = "Relatório Semestral"
        verbose_name_plural = "Relatórios Semestrais"

    def __str__(self):
        return f"{self.aluno.nome} - {self.semestre}"


