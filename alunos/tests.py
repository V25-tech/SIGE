from django.test import TestCase
from .models import Aluno, Responsavel


class AlunoModelTest(TestCase):

    def setUp(self):

        self.responsavel = Responsavel.objects.create(
            nome="Maria Silva",
            cpf="12345678900",
            telefone="11999999999"
        )

    def test_criacao_aluno(self):

        aluno = Aluno.objects.create(
            nome="João Teste",
            matricula="2026001",
            data_nascimento="2018-01-01",
            turma="1º Ano A",
            responsavel=self.responsavel
        )

        self.assertEqual(
            aluno.nome,
            "João Teste"
        )