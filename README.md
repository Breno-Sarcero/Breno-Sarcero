<p align="center">
  <img src="assets/header-v3.svg" alt="Terminal: Olá, sejam bem-vindos todos! Breno Sarcero, Dev Júnior de IA, cursando ADS na FMU" width="820">
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

<table>
  <tr>
    <td><b>IA e agentes</b></td>
    <td><img src="assets/tiles-ia-v1.svg" alt="Claude Code, MCP, Playwright" height="48"></td>
  </tr>
  <tr>
    <td><b>Back-end e web</b></td>
    <td><img src="https://skillicons.dev/icons?theme=dark&i=python,django,ts,js,html,css" alt="Python, Django, TypeScript, JavaScript, HTML, CSS" height="48"></td>
  </tr>
  <tr>
    <td><b>Dados</b></td>
    <td><img src="assets/tiles-dados-v1.svg" alt="SQL Server, Power BI, Questor ERP" height="48"></td>
  </tr>
  <tr>
    <td><b>Ferramentas</b></td>
    <td><img src="https://skillicons.dev/icons?theme=dark&i=git,github,powershell" alt="Git, GitHub, PowerShell" height="48"></td>
  </tr>
</table>

## Contato

<a href="https://www.linkedin.com/in/breno-santiago-sarcero"><img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn" height="40"></a>
<a href="mailto:santiagobreno6@gmail.com"><img src="https://skillicons.dev/icons?i=gmail" alt="E-mail" height="40"></a>
