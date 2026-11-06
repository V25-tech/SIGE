from django.shortcuts import render
from django.http import HttpResponse

from reportlab.pdfgen import canvas

from alunos.models import Aluno, Responsavel
from documentos.models import Documento

from pedagogico.models import (
    Nota,
    ParecerProfessor,
    HistoricoEscolar,
    RelatorioSemestral,
    Entrega
)


def home(request):

    total_alunos = Aluno.objects.count()
    total_responsaveis = Responsavel.objects.count()
    total_documentos = Documento.objects.count()

    return render(
        request,
        'home.html',
        {
            'total_alunos': total_alunos,
            'total_responsaveis': total_responsaveis,
            'total_documentos': total_documentos,
        }
    )


def lista_alunos(request):

    alunos = Aluno.objects.all()

    return render(
        request,
        'alunos.html',
        {
            'alunos': alunos
        }
    )


def relatorio_pais(request):

    alunos = Aluno.objects.all()

    if request.method == 'POST':

        aluno_id = request.POST.get('aluno')

        aluno = Aluno.objects.get(
            id=aluno_id
        )

        response = HttpResponse(
            content_type='application/pdf'
        )

        response[
            'Content-Disposition'
        ] = 'attachment; filename="relatorio_pais.pdf"'

        pdf = canvas.Canvas(response)

        pdf.drawString(
            100,
            750,
            'RELATORIO PEDAGOGICO'
        )

        pdf.drawString(
            100,
            720,
            f'Aluno: {aluno.nome}'
        )

        pdf.drawString(
            100,
            700,
            f'Turma: {aluno.turma}'
        )

        pdf.drawString(
            100,
            680,
            f'Responsavel: {aluno.responsavel.nome}'
        )

        y = 640

        pdf.drawString(
            100,
            y,
            'NOTAS'
        )

        y -= 30

        notas = Nota.objects.filter(
            aluno=aluno
        )

        for nota in notas:

            pdf.drawString(
                120,
                y,
                f'{nota.disciplina}: {nota.nota}'
            )

            y -= 20

        y -= 20

        relatorios = RelatorioSemestral.objects.filter(
            aluno=aluno
        )

        for relatorio in relatorios:

            pdf.drawString(
                100,
                y,
                f'Faltas: {relatorio.faltas}'
            )

            y -= 20

            pdf.drawString(
                100,
                y,
                f'Observacoes: {relatorio.observacoes}'
            )

            y -= 30

        pareceres = ParecerProfessor.objects.filter(
            aluno=aluno
        )

        for parecer in pareceres:

            pdf.drawString(
                100,
                y,
                'PARECER DO PROFESSOR'
            )

            y -= 20

            pdf.drawString(
                120,
                y,
                parecer.parecer[:100]
            )

            y -= 20

            pdf.drawString(
                120,
                y,
                f'Pontos a melhorar: {parecer.pontos_melhorar[:80]}'
            )

            y -= 30

        entregas = Entrega.objects.filter(
            aluno=aluno
        )

        pdf.drawString(
            100,
            y,
            'ENTREGAS REGISTRADAS'
        )

        y -= 20

        for entrega in entregas:

            pdf.drawString(
                120,
                y,
                f'{entrega.tipo} - {entrega.data_entrega}'
            )

            y -= 20

        pdf.save()

        return response

    return render(
        request,
        'relatorio_pais.html',
        {
            'alunos': alunos
        }
    )


def emitir_declaracao(request):

    alunos = Aluno.objects.all()

    if request.method == 'POST':

        aluno_id = request.POST.get('aluno')
        aluno = Aluno.objects.get(id=aluno_id)

        tipo = request.POST.get('tipo')

        responsavel = aluno.responsavel.nome

        data_retirada = request.POST.get(
            'data_retirada'
        )

        Documento.objects.create(
            aluno=aluno,
            tipo_documento=tipo
        )

        if tipo in ['uniforme', 'material']:

            Entrega.objects.create(
                aluno=aluno,
                responsavel=aluno.responsavel,
                tipo=tipo,
                data_entrega=data_retirada,
                observacoes='Entrega registrada pelo SIGE'
            )

        response = HttpResponse(
            content_type='application/pdf'
        )

        response[
            'Content-Disposition'
        ] = 'attachment; filename="documento.pdf"'

        pdf = canvas.Canvas(response)

        titulos = {
            'matricula': 'DECLARACAO DE MATRICULA',
            'frequencia': 'DECLARACAO DE FREQUENCIA',
            'transferencia': 'DECLARACAO DE TRANSFERENCIA',
            'historico': 'HISTORICO ESCOLAR',
            'uniforme': 'RECEBIMENTO DE UNIFORME',
            'material': 'RECEBIMENTO DE MATERIAL ESCOLAR',
            'participacao': 'PARTICIPACAO EM PROJETOS',
            'apm': 'PRESTACAO DE CONTAS APM'
        }

        pdf.drawString(
            100,
            750,
            titulos.get(tipo, 'DOCUMENTO ESCOLAR')
        )

        pdf.drawString(
            100,
            700,
            f'Aluno: {aluno.nome}'
        )

        pdf.drawString(
            100,
            680,
            f'Matricula: {aluno.matricula}'
        )

        pdf.drawString(
            100,
            660,
            f'Turma: {aluno.turma}'
        )

        if tipo == 'uniforme':

            pdf.drawString(
                100,
                620,
                f'Responsavel: {responsavel}'
            )

            pdf.drawString(
                100,
                600,
                f'Data da retirada: {data_retirada}'
            )

            pdf.drawString(
                100,
                580,
                'Itens entregues:'
            )

            pdf.drawString(
                120,
                560,
                '- Camiseta'
            )

            pdf.drawString(
                120,
                540,
                '- Calca'
            )

            pdf.drawString(
                120,
                520,
                '- Agasalho'
            )

        elif tipo == 'material':

            pdf.drawString(
                100,
                620,
                f'Responsavel: {responsavel}'
            )

            pdf.drawString(
                100,
                600,
                f'Data da retirada: {data_retirada}'
            )

            pdf.drawString(
                100,
                580,
                'Materiais entregues:'
            )

            pdf.drawString(
                120,
                560,
                '- Caderno'
            )

            pdf.drawString(
                120,
                540,
                '- Lapis'
            )

            pdf.drawString(
                120,
                520,
                '- Borracha'
            )

            pdf.drawString(
                120,
                500,
                '- Estojo'
            )

        else:

            pdf.drawString(
                100,
                620,
                'Documento emitido automaticamente'
            )

            pdf.drawString(
                100,
                600,
                'pelo Sistema Integrado de Gestao Escolar.'
            )

        pdf.drawString(
            100,
            520,
            'EMEB Dionysio Bovo'
        )

        pdf.drawString(
            100,
            500,
            'SIGE'
        )

        pdf.drawString(
            100,
            480,
            'Sistema Integrado de Gestao Escolar'
        )

        pdf.save()

        return response

    return render(
        request,
        'emitir_declaracao.html',
        {
            'alunos': alunos
        }
    )