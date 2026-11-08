web: gunicorn sige.wsgi
reportlab==5.1.0

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Dashboard da Direção</title>
</head>
<body>

<h1>📊 Dashboard da Direção</h1>

<h2>Indicadores Pedagógicos</h2>

<p>Total de Matriculados: {{ total_matriculados }}</p>
<p>Total de Participantes: {{ total_participantes }}</p>
<p>Total de Faltosos: {{ total_faltosos }}</p>
<p>Participação: {{ participacao }}%</p>
<p>Acima da Meta: {{ total_acima_meta }}</p>
<p>Abaixo da Meta: {{ total_abaixo_meta }}</p>

<hr>

<h2>💰 Financeiro APM</h2>

<p>Arrecadação: R$ {{ arrecadacao }}</p>
<p>Despesas: R$ {{ despesas }}</p>
<p>Saldo: R$ {{ saldo }}</p>

<p>
<a href="/">Voltar ao SIGE</a>
</p>

</body>
</html>
