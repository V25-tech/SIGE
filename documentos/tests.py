from django.test import TestCase
from alunos.models import Aluno, Responsavel
from .models import Documento


class DocumentoTest(TestCase):

    def setUp(self):

        resp = Responsavel.objects.create(
            nome="Maria Silva",
            cpf="12345678900",
            telefone="11999999999"
        )

        self.aluno = Aluno.objects.create(
            nome="João Teste",
            matricula="2026001",
            data_nascimento="2018-01-01",
            turma="1º Ano A",
            responsavel=resp
        )

    def test_documento(self):

        doc = Documento.objects.create(
            aluno=self.aluno,
            tipo_documento="Declaração"
        )

        self.assertEqual(
            doc.tipo_documento,
            "Declaração"
        )