<p align="center">
  <img src="assets/header-v2.svg" alt="Terminal: Olá, sejam bem-vindos todos! Breno Sarcero, Dev Júnior de IA, cursando ADS na FMU" width="820">
</p>

## Sobre mim

Estudante de Análise e Desenvolvimento de Sistemas na FMU. Hoje desenvolvo sites e soluções para a área contábil, além de dashboards em Power BI. Atuo de ponta a ponta (full stack):

- **Back-end e web:** sistemas internos em Django, com integração por API ao ERP Questor.
- **Banco de dados:** modelagem de tabelas limpas e organizadas no SQL Server.
- **Procedures:** tratamento e transformação dos dados para que cheguem corretos às telas e aos relatórios.
- **Power BI:** dashboards construídos sobre esses dados já tratados.

Entusiasta de IA: uso o Claude Code como parte do fluxo de desenvolvimento e crio plugins para deixá-lo mais seguro e mais prático.

<p align="center">
  <img src="assets/agent-v3.svg" alt="Mascote que dorme, acorda com um comando, trabalha, se irrita com um erro, corrige e comemora" width="820">
</p>

## Como trabalho com IA

Não uso IA só para conversar: monto agentes que fazem o trabalho de ponta a ponta, com revisão humana no fim.

- **Orquestração de subagentes:** um modelo maior planeja e distribui as tarefas para modelos menores e mais baratos, que rodam em paralelo.
- **Pipeline de segurança com três modelos:** um procura vulnerabilidades, outro aplica a correção e um terceiro valida.
- **Servidores MCP:** conectam o Claude ao SQL Server e ao navegador, com trava de escrita (o [sql-guard](https://github.com/Breno-Sarcero/sql-guard)).
- **Plugins e hooks para o Claude Code:** ajustam o comportamento do agente ao meu fluxo.

<p align="center">
  <img src="assets/flow.svg?v=2" alt="Fluxo agêntico: você, orquestrador, subagentes, ferramentas MCP e PR revisado" width="820">
</p>

## Projetos em destaque

### [sql-guard](https://github.com/Breno-Sarcero/sql-guard)

Plugin para o Claude Code que exige duas confirmações explícitas antes de qualquer escrita ou DDL em SQL, venha pelas ferramentas MCP do SQL Server ou por comandos de banco no terminal. Tudo fica registrado em log de auditoria.

<img src="https://github.com/Breno-Sarcero/sql-guard/raw/main/docs/demo-pt.gif" alt="sql-guard bloqueando um DELETE até a dupla confirmação" width="720">

### [usage-bar](https://github.com/Breno-Sarcero/usage-bar)

Plugin para o Claude Code que mostra uma barra de uso acima do prompt, com janela de contexto e limites de uso (5h e semana), em português ou inglês.

<img src="https://github.com/Breno-Sarcero/usage-bar/raw/main/docs/demo-pt.gif" alt="usage-bar acompanhando contexto, 5h e semana acima do prompt" width="720">

### Outros

- [IsyShell](https://github.com/Breno-Sarcero/isyshell): microsserviço para execução remota e segura de shell scripts via API REST. Hackathon FMU Tech 2026.

### Em construção

- [UNO](https://github.com/Breno-Sarcero/UNO): assistente pessoal de voz no estilo Alexa, rodando 100% em hardware próprio (ESP32 + LLM local, com tool-calling). Em fase de arquitetura.

## Stack

**IA e agentes**

![Claude Code](https://img.shields.io/badge/Claude%20Code-1c1917?style=for-the-badge&logo=claude&logoColor=f59e0b)
![MCP](https://img.shields.io/badge/MCP-1c1917?style=for-the-badge&logo=modelcontextprotocol&logoColor=f59e0b)
![Playwright](https://img.shields.io/badge/Playwright-1c1917?style=for-the-badge)

**Linguagens**

![Python](https://img.shields.io/badge/Python-1c1917?style=for-the-badge&logo=python&logoColor=f59e0b)
![TypeScript](https://img.shields.io/badge/TypeScript-1c1917?style=for-the-badge&logo=typescript&logoColor=f59e0b)
![SQL](https://img.shields.io/badge/SQL-1c1917?style=for-the-badge&logo=databricks&logoColor=f59e0b)

**Frameworks e banco de dados**

![Django](https://img.shields.io/badge/Django-1c1917?style=for-the-badge&logo=django&logoColor=f59e0b)
![SQL Server](https://img.shields.io/badge/SQL%20Server-1c1917?style=for-the-badge&logo=microsoftsqlserver&logoColor=f59e0b)
![REST APIs](https://img.shields.io/badge/REST%20APIs-1c1917?style=for-the-badge&logo=swagger&logoColor=f59e0b)

**Ferramentas**

![Power BI](https://img.shields.io/badge/Power%20BI-1c1917?style=for-the-badge)
![Questor ERP](https://img.shields.io/badge/Questor%20ERP-1c1917?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-1c1917?style=for-the-badge&logo=git&logoColor=f59e0b)
![GitHub](https://img.shields.io/badge/GitHub-1c1917?style=for-the-badge&logo=github&logoColor=f59e0b)

## Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-1c1917?style=for-the-badge&logo=linkedin&logoColor=f59e0b)](https://www.linkedin.com/in/breno-santiago-sarcero)
[![E-mail](https://img.shields.io/badge/E--mail-1c1917?style=for-the-badge&logo=gmail&logoColor=f59e0b)](mailto:santiagobreno6@gmail.com)
