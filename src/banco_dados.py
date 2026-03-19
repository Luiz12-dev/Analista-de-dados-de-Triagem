import sqlite3
from typing import List, Dict, Any

def inicializar_banco(nome_banco: str = "triagem_database.db") -> None:
    """
    Cria e configura o banco de dados inicial (pacientes_validados) com as colunas certas.
    """
    with sqlite3.connect(nome_banco) as conexao:
        cursor = conexao.cursor()
        
        # Cria a tabela caso não exista
        query = """
        CREATE TABLE IF NOT EXISTS pacientes_validados (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            sintoma TEXT NOT NULL,
            nivel_urgencia INTEGER NOT NULL,
            tempo_espera_minutos INTEGER NOT NULL
        )
        """
        cursor.execute(query)
        conexao.commit()

def salvar_dados_lote(dados: List[Dict[str, Any]], nome_banco: str = "triagem_database.db") -> None:
    """
    Recebe os dados limpos listados/estruturados, reseta a tabela (opcional, p/ PoC iterativo),
    e salva-os no banco através de um INSERT estritamente em lote (batch API do SQLite).
    """
    if not dados:
        print(" -> Nenhum dado para salvar.")
        return
        
    with sqlite3.connect(nome_banco) as conexao:
        cursor = conexao.cursor()
        
        # Limpar os dados pré-existentes na tabela para evitar id duplicado nas sucessivas execuções desta PoC
        cursor.execute("DELETE FROM pacientes_validados")
        
        # Inserção em lote (executemany) que é uma excelente prática
        query = """
        INSERT INTO pacientes_validados 
        (id, nome, idade, sintoma, nivel_urgencia, tempo_espera_minutos)
        VALUES (:id, :nome, :idade, :sintoma, :nivel_urgencia, :tempo_espera_minutos)
        """
        
        cursor.executemany(query, dados)
        conexao.commit()

def exibir_relatorio_analitico(nome_banco: str = "triagem_database.db") -> None:
    """
    Executa a Query SQL analítica para média de tempo agrupado pelo nível de urgencia e exibe pro terminal. 
    """
    with sqlite3.connect(nome_banco) as conexao:
        cursor = conexao.cursor()
        
        query = """
        SELECT 
            nivel_urgencia, 
            AVG(tempo_espera_minutos) AS tempo_medio,
            COUNT(*) as pacientes_atendidos
        FROM pacientes_validados
        GROUP BY nivel_urgencia
        ORDER BY nivel_urgencia DESC
        """
        
        cursor.execute(query)
        resultados = cursor.fetchall()

        print("-" * 50)
        print(" RELATÓRIO: Tempo Médio de Espera Por Urgência ")
        print("-" * 50)
        print("Urgência | Média de Espera (min) | Qtd Pacientes")
        for nivel_urgencia, tempo_medio, quantidade in resultados:
            print(f"   {nivel_urgencia}     |       {tempo_medio:^15.1f}   |   {quantidade}")
        print("-" * 50)
