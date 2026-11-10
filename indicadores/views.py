from django.shortcuts import render
import pandas as pd

from .models import (
    AvaliacaoExterna,
    APM
)


def dashboard_direcao(request):

    avaliacoes = AvaliacaoExterna.objects.all()

    total_matriculados = sum(
        a.matriculados for a in avaliacoes
    )

    total_participantes = sum(
        a.participantes for a in avaliacoes
    )

    total_faltosos = sum(
        a.faltosos for a in avaliacoes
    )

    total_acima_meta = sum(
        a.acima_meta for a in avaliacoes
    )

    total_abaixo_meta = sum(
        a.abaixo_meta for a in avaliacoes
    )

    participacao = 0
    percentual_faltosos = 0
    percentual_acima_meta = 0
    percentual_abaixo_meta = 0

    if total_matriculados > 0:

        participacao = (
            total_participantes /
            total_matriculados
        ) * 100

        percentual_faltosos = (
            total_faltosos /
            total_matriculados
        ) * 100

    if total_participantes > 0:

        percentual_acima_meta = (
            total_acima_meta /
            total_participantes
        ) * 100

        percentual_abaixo_meta = (
            total_abaixo_meta /
            total_participantes
        ) * 100

    comparativo_turmas = []

    for avaliacao in avaliacoes:

        participacao_turma = 0

        if avaliacao.matriculados > 0:

            participacao_turma = (
                avaliacao.participantes /
                avaliacao.matriculados
            ) * 100

        comparativo_turmas.append(
            {
                'avaliacao':
                    avaliacao.avaliacao,

                'data':
                    avaliacao.data,

                'turma':
                    avaliacao.turma,

                'matriculados':
                    avaliacao.matriculados,

                'participantes':
                    avaliacao.participantes,

                'faltosos':
                    avaliacao.faltosos,

                'acima_meta':
                    avaliacao.acima_meta,

                'abaixo_meta':
                    avaliacao.abaixo_meta,

                'participacao':
                    round(
                        participacao_turma,
                        2
                    )
            }
        )

    comparativo_turmas.sort(
        key=lambda x: x['participacao'],
        reverse=True
    )

    ultima_avaliacao = None

    if avaliacoes.exists():

        ultima_avaliacao = (
            avaliacoes
            .order_by('-data')
            .first()
        )

    meses_apm = APM.objects.all().order_by(
        '-ano',
        '-mes'
    )

    total_arrecadado = sum(
        item.arrecadacao
        for item in meses_apm
    )

    total_despesas = sum(
        item.despesas
        for item in meses_apm
    )

    saldo_total = 0

    if meses_apm.exists():

        saldo_total = (
            meses_apm.first().saldo_final
        )

    return render(
        request,
        'indicadores/dashboard.html',
        {
            'total_matriculados':
                total_matriculados,

            'total_participantes':
                total_participantes,

            'total_faltosos':
                total_faltosos,

            'total_acima_meta':
                total_acima_meta,

            'total_abaixo_meta':
                total_abaixo_meta,

            'participacao':
                round(
                    participacao,
                    2
                ),

            'percentual_faltosos':
                round(
                    percentual_faltosos,
                    2
                ),

            'percentual_acima_meta':
                round(
                    percentual_acima_meta,
                    2
                ),

            'percentual_abaixo_meta':
                round(
                    percentual_abaixo_meta,
                    2
                ),

            'comparativo_turmas':
                comparativo_turmas,

            'ultima_avaliacao':
                ultima_avaliacao,

            'meses_apm':
                meses_apm,

            'total_arrecadado':
                total_arrecadado,

            'total_despesas':
                total_despesas,

            'saldo_total':
                saldo_total,
        }
    )


def historico_apm(request):

    registros = APM.objects.all().order_by(
        '-ano',
        '-mes'
    )

    return render(
        request,
        'indicadores/historico_apm.html',
        {
            'registros': registros
        }
    )


def importar_planilha(request):

    mensagem = ""

    if request.method == "POST":

        arquivo = request.FILES.get("arquivo")

        if arquivo:

            df = pd.read_excel(
                arquivo,
                engine="openpyxl"
            )

            mensagem = (
                f"Planilha importada com "
                f"{len(df)} linhas."
            )

    return render(
        request,
        'indicadores/importar_planilha.html',
        {
            'mensagem': mensagem
        }
    )