from django.shortcuts import render
from django.http import HttpResponse

from reportlab.pdfgen import canvas

from alunos.models import Aluno
from alunos.models import Responsavel
from documentos.models import Documento


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


def emitir_declaracao(request):

    alunos = Aluno.objects.all()

    if request.method == 'POST':

        aluno_id = request.POST.get('aluno')

        aluno = Aluno.objects.get(id=aluno_id)

        Documento.objects.create(
            aluno=aluno,
            tipo_documento='Declaração de Matrícula'
        )

        response = HttpResponse(
            content_type='application/pdf'
        )

        response[
            'Content-Disposition'
        ] = 'attachment; filename="declaracao.pdf"'

        pdf = canvas.Canvas(response)

        pdf.drawString(
            100,
            750,
            'DECLARACAO DE MATRICULA'
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

        pdf.drawString(
            100,
            620,
            'Declaramos que o aluno encontra-se'
        )

        pdf.drawString(
            100,
            600,
            'regularmente matriculado na'
        )

        pdf.drawString(
            100,
            580,
            'EMEB Dionysio Bovo.'
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