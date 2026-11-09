# 📚⚙️ SIGE

## Sistema Integrado de Gestão Escolar

O **SIGE (Sistema Integrado de Gestão Escolar)** é uma aplicação web desenvolvida em **Python/Django** para apoiar a gestão administrativa, financeira e pedagógica das instituições de ensino.

O projeto foi desenvolvido para a **EMEB Dionysio Bovo**, com o objetivo de centralizar informações escolares, automatizar processos internos e disponibilizar indicadores para auxiliar a tomada de decisões da equipe gestora.

---

# 🎯 Objetivo

Fornecer uma plataforma integrada que auxilie a gestão escolar, automatize processos administrativos e contribua para o acompanhamento pedagógico dos alunos por meio de indicadores e relatórios gerenciais.

---

# 🌐 Sistema Publicado

O SIGE encontra-se disponível online através da plataforma Render:

🔗 [https://sige-l7do.onrender.com](https://sige-l7do.onrender.com)

---

# 🏫 Funcionalidades Administrativas

✅ Cadastro de Alunos

✅ Cadastro de Responsáveis

✅ Consulta de Alunos

✅ Emissão de Declarações

✅ Registro de Documentos

✅ Dashboard Inicial

✅ Administração via Django Admin

✅ Geração de PDF

✅ Controle Financeiro da APM

✅ Histórico Financeiro da APM

✅ Importação de Planilhas Excel

---

# 📊 Funcionalidades Pedagógicas

✅ Avaliações Externas (SAREM, SAEB, Provinha Paulista)

✅ Indicadores Pedagógicos

✅ Dashboard da Direção

✅ Comparativo por Turma

✅ Controle de Participação em Avaliações

✅ Monitoramento de alunos acima e abaixo da meta

✅ Plano de Melhoria

✅ Planejamento de Aula

✅ Reuniões HTPC

✅ Reuniões com Pais

✅ Acompanhamento da Aprendizagem

✅ Monitoramento de componentes curriculares

✅ Identificação de conteúdos abaixo da meta prevista

---

# 📈 Dashboard da Direção

O módulo Dashboard foi desenvolvido para fornecer informações consolidadas à equipe gestora.

### Indicadores Pedagógicos

- Total de alunos matriculados
- Total de participantes
- Total de faltosos
- Percentual de participação
- Percentual de alunos acima da meta
- Percentual de alunos abaixo da meta

### Indicadores Financeiros

- Total arrecadado pela APM
- Total de despesas
- Saldo acumulado
- Histórico financeiro mensal

### Comparativo por Turma

- Participação por turma
- Quantidade de participantes
- Quantidade de faltosos
- Alunos acima da meta
- Alunos abaixo da meta

---

# 💰 Módulo Financeiro APM

O SIGE permite registrar o acompanhamento financeiro da Associação de Pais e Mestres.

### Controle Mensal

- Mês
- Ano
- Saldo Inicial
- Arrecadação
- Despesas
- Saldo Final

### Exemplo

Outubro/2026

- Saldo Inicial: R$ 0,00
- Arrecadação: R$ 1.000,00
- Despesas: R$ 500,00
- Saldo Final: R$ 500,00

O saldo final pode ser utilizado como saldo inicial do período seguinte.

---

# 📝 Avaliações Externas

Permite registrar resultados de avaliações institucionais por turma.

### Dados Registrados

- Avaliação
- Data
- Turma
- Alunos matriculados
- Participantes
- Faltosos
- Alunos acima da meta
- Alunos abaixo da meta

### Exemplo

SAREM – 03/10/2026

Turma: 5º B

- Matriculados: 30
- Participantes: 20
- Faltosos: 10
- Acima da Meta: 14
- Abaixo da Meta: 9

---

# 📁 Importação de Planilhas

Foi desenvolvido um módulo para importação de arquivos Excel.

### Objetivo

Reduzir retrabalho da equipe escolar e evitar duplicidade de digitação.

### Tecnologias utilizadas

- Pandas
- OpenPyXL

A funcionalidade permitirá futuramente alimentar automaticamente os indicadores pedagógicos e financeiros a partir das planilhas utilizadas pela escola.

---

# 🛠️ Tecnologias Utilizadas

🐍 Python

🌐 Django

🗄️ SQLite

📊 Chart.js

📈 Pandas

📄 OpenPyXL

📄 ReportLab

🎨 HTML5

🎨 CSS3

🔧 Git

🐙 GitHub

☁️ Render

🤍 WhiteNoise

---

# 🔄 Fluxo Principal

🏠 Menu Principal

        ↓

👨‍🎓 Consulta de Alunos

        ↓

✅ Selecionar Aluno

        ↓

📄 Emitir Declaração

        ↓

📑 Gerar PDF

        ↓

📝 Registrar Emissão

---

# 📊 Fluxo dos Indicadores Pedagógicos

👨‍🏫 Professor

        ↓

📝 Lança resultado da avaliação

        ↓

📊 SIGE consolida os dados

        ↓

📈 Dashboard da Direção

        ↓

📋 Relatórios Gerenciais

---

# 💰 Fluxo da APM

💰 Registro Financeiro

        ↓

📥 Arrecadação

        ↓

📤 Despesas

        ↓

📊 Saldo Final

        ↓

📅 Histórico Financeiro

---

# 📷 Capturas de Tela

## 🏠 Dashboard Inicial

![Dashboard](InvalidUrl)

---

## 📊 Dashboard da Direção

![Dashboard Direção](InvalidUrl)

---

## 📄 Emissão de Declaração

![Declaração](InvalidUrl)

---

## ⚙️ Administração do Sistema

![Admin](InvalidUrl)

---

# 🗂️ Estrutura do Projeto

SIGE

│

├── alunos

├── documentos

├── pedagogico

├── indicadores

├── contas

├── sige

├── static

├── templates

├── screenshots

│

├── README.md

├── requirements.txt

├── Procfile

├── .gitignore

└── manage.py

---

# 👥 Público\-Alvo

- Direção Escolar
- Secretaria Escolar
- Coordenação Pedagógica
- Professores
- Equipe Administrativa

---

# 🌎 ODS Relacionado

## ODS 4 – Educação de Qualidade

O projeto contribui para a melhoria dos processos administrativos, financeiros e pedagógicos da escola, apoiando a gestão educacional por meio da tecnologia.

---

# 👩‍💻 Autora

**Vanusa A. Ferreira**

🔗 GitHub: [https://github.com/V25-tech/SIGE](https://github.com/V25-tech/SIGE)

🔗 LinkedIn: [https://lnkd.in/p/du3dbrqm](https://lnkd.in/p/du3dbrqm)

🔗 Sistema Online: [https://sige-l7do.onrender.com](https://sige-l7do.onrender.com)

Projeto desenvolvido para fins acadêmicos.

---

# 🙏 Agradecimentos

Gostaria de expressar meus sinceros agradecimentos ao **Diretor Marcos Paulo**, da **EMEB Dionysio Bovo**, pela disponibilidade, apoio e participação durante o desenvolvimento deste projeto.

Sua colaboração foi fundamental ao responder ao levantamento de requisitos, compartilhar informações sobre a realidade da gestão escolar e contribuir com sugestões para evolução do sistema.

As necessidades apresentadas pela equipe gestora motivaram a implementação de funcionalidades como:

- 📊 Dashboard da Direção
- 🏫 Comparativo por Turma
- 💰 Controle Financeiro da APM
- 📅 Histórico Financeiro
- 📝 Avaliações Externas
- 📁 Importação de Planilhas Excel
- 🎯 Plano de Melhoria
- 👨‍🏫 HTPC
- 👨‍👩‍👧 Reuniões com Pais
- 📚 Acompanhamento da Aprendizagem

Agradeço pela confiança, receptividade e contribuição para a construção deste projeto acadêmico.

---

## 💙 SIGE

**Conectando Educação, Gestão e Tecnologia**

