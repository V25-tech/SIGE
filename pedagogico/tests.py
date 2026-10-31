from django.test import TestCase
from .models import IndicadorPedagogico


class IndicadorTest(TestCase):

    def test_indicador(self):

        indicador = IndicadorPedagogico.objects.create(
            ano_escolar="1º Ano",
            componente="Matemática",
            meta_mec=70,
            resultado=52,
            observacoes="Teste"
        )

        self.assertEqual(
            indicador.componente,
            "Matemática"
        )