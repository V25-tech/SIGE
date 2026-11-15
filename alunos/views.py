from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .models import (
    Aluno,
    BuscaAtiva
)


def pagina_inicial(request):

    return render(
        request,
        'home.html'
    )


def alunos_home(request):

    alunos = Aluno.objects.all()

    return render(
        request,
        'alunos/lista_alunos.html',
        {
            'alunos': alunos
        }
    )


def busca_ativa(request):

    registros = BuscaAtiva.objects.all()

    return render(
        request,
        'alunos/busca_ativa.html',
        {
            'registros': registros
        }
    )


def relatorio_conselho(request, pk):

    registro = BuscaAtiva.objects.get(
        id=pk
    )

    historicos = registro.historicos.all()

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = (
        f'attachment; '
        f'filename="busca_ativa_{pk}.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.setTitle(
        "Relatório Busca Ativa"
    )

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    y = 800

    pdf.drawString(
        50,
        y,
        "RELATÓRIO DE BUSCA ATIVA"
    )

    pdf.setFont(
        "Helvetica",
        10
    )

    y -= 40

    pdf.drawString(
        50,
        y,
        f"Aluno: {registro.aluno.nome}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Turma: {registro.aluno.turma}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Quantidade de faltas: "
        f"{registro.quantidade_faltas}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Motivo das faltas: "
        f"{registro.motivo_faltas}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Possui atestado: "
        f"{'Sim' if registro.possui_atestado else 'Não'}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Responsável contatado: "
        f"{registro.responsavel_contato}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Telefone: "
        f"{registro.telefone_contato}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Contato telefônico: "
        f"{'Sim' if registro.contato_telefonico else 'Não'}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Visita domiciliar: "
        f"{'Sim' if registro.visita_domiciliar else 'Não'}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Professor responsável: "
        f"{registro.professor_responsavel}"
    )

    y -= 30

    pdf.drawString(
        50,
        y,
        "Observações:"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        registro.observacoes or "-"
    )

    y -= 50

    pdf.setFont(
        "Helvetica-Bold",
        12
    )

    pdf.drawString(
        50,
        y,
        "HISTÓRICO DE CONTATOS"
    )

    pdf.setFont(
        "Helvetica",
        10
    )

    for contato in historicos:

        if y < 120:

            pdf.showPage()

            y = 800

        y -= 25

        pdf.drawString(
            50,
            y,
            f"{contato.data_contato}"
        )

        y -= 20

        pdf.drawString(
            70,
            y,
            f"Tipo: {contato.tipo_contato}"
        )

        y -= 20

        pdf.drawString(
            70,
            y,
            f"Responsável: "
            f"{contato.responsavel_falou}"
        )

        y -= 20

        pdf.drawString(
            70,
            y,
            f"Observações: "
            f"{contato.observacoes}"
        )

    pdf.save()

    return response