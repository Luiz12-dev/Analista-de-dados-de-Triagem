# Triagem Data Analyzer 🏥📊

Este projeto é uma Prova de Conceito (PoC) desenvolvida em Python para uma empresa HealthTech, demonstrando habilidades fundamentais em **Engenharia de Dados**, **Limpeza de Dados** e **Análise de Dados**. 

O sistema simula um pipeline de dados ponta-a-ponta para analisar tempos de espera na triagem de um hospital ou clínica.

## 🚀 Funcionalidades (O Pipeline)

A execução principal (`main.py`) orquestra um fluxo de dados estruturado em 4 etapas:

1. **Geração de Dados (Mock):** Cria um arquivo CSV (`dados/pacientes_raw.csv`) contendo registros de pacientes gerados proceduralmente. O gerador introduz "ruídos" intencionais (dados sujos), como idades negativas e valores nulos em campos obrigatórios, para simular desafios reais.
2. **Processamento e Limpeza (Data Cleaning):** Lê o CSV ruidoso e aplica regras de negócio para validar e limpar os dados, descartando registros inválidos e estruturando a informação de forma segura na memória.
3. **Persistência em Banco de Dados Relacional:** Inicializa automaticamente um banco de dados SQLite local (`triagem_database.db`) e insere os dados validados em lote (_batch insert_ usando `executemany`), demonstrando boas práticas de performance.
4. **Analytics (Relatório Analítico):** Executa uma _query_ SQL analítica de agregação (no SQLite) para calcular e exibir a **média do tempo de espera agrupada por nível de urgência**, apresentando um relatório de resumo diretamente no terminal.

## 📂 Estrutura do Projeto

* `main.py`: Arquivo principal e orquestrador que executa todo o pipeline passo-a-passo.
* `src/gerador_dados.py`: Responsável por simular e gerar os dados sujos em CSV.
* `src/processador.py`: Motor de limpeza e curadoria, responsável por aplicar as regras de negócio / validação dos dados.
* `src/banco_dados.py`: Gerencia a conexão, criação de tabelas, inserção eficiente (bulk) no SQLite e geração do relatório (SQL).
* `dados/`: Diretório de saída/entrada temporária onde o CSV `pacientes_raw.csv` é gerado.
* `requirements.txt`: Arquivo não contem dependências visto que a PoC foca em bibliotecas de core.

## 🛠️ Tecnologias Utilizadas

* **Python 3+**
* **Bibliotecas Padrão:** `csv`, `sqlite3`, `os`, `random`, `typing` (Foco em programação procedural estruturada, sem abstrações pesadas como Pandas ou ORMs).
* **Banco de Dados:** SQLite (em memória/disco), escolhido por ser o modelo ideal _out-of-the-box_ para PoCs.

## ⚙️ Como Executar

Por utilizar exclusivamente bibliotecas embutidas no interpretador Python, a execução é extremamente simples. Não é necessário instalar pacotes locais/externos adicionais via `pip`.

1. Clone ou acesse o repositório em sua máquina.
2. Abra o terminal na raiz do projeto (`/triagem-data-analyzer`).
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Acompanhe os _logs_ detalhados no terminal que indicam todas as interações e a demonstração analítica das tabelas.

## 💡 Observações do PoC

* **Resiliência:** Mesmo com valores vazios inesperados ("") na sintaxe gerada, o sistema descarta sem quebrar.
* **Desempenho (Batch Query):** A tabela conta com inserção bulk (`executemany`), prevendo um passo à frente visando escalabilidade em caso de Big Data.
* **Tipagem:** O uso do módulo `typing` facilita bastante a leitura do código, permitindo previsões mais precisas de Dicionários e Listas ao decorrer do trânsito de dados do SQLite.
