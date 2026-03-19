import os
import csv
import random

def gerar_dados(caminho_arquivo: str = "dados/pacientes_raw.csv", quantidade: int = 50) -> None:
    """
    Gera um arquivo CSV com dados fictícios de pacientes.
    Insere intencionalmente dados 'sujos' para simular um cenário real de limpeza de dados.
    """
    # Garante que o diretório 'dados' ou qualquer outro pai do arquivo exista
    diretorio = os.path.dirname(caminho_arquivo)
    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio)
        
    nomes_base = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia"]
    sintomas = ["Dor de cabeça", "Febre", "Tosse", "Dor no peito", "Falta de ar", "Náusea", "Tontura", "Dor abdominal"]
    
    dados = []
    for i in range(1, quantidade + 1):
        nome = f"{random.choice(nomes_base)} Silva {i}"
        
        # Insere idades inválidas (negativas) estatisticamente (ex: 10% de chance)
        idade = random.randint(18, 90) if random.random() > 0.1 else random.randint(-10, -1)
        
        sintoma = random.choice(sintomas)
        
        # Insere nível de urgência em branco (10% de chance)
        urgencia = random.randint(1, 5) if random.random() > 0.1 else ""
        
        # Insere tempo de espera nulo/vazio (10% de chance)
        tempo = random.randint(0, 240) if random.random() > 0.1 else ""
        
        dados.append([i, nome, idade, sintoma, urgencia, tempo])

    # Cria o arquivo CSV e escreve os dados
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        # Escreve o cabeçalho
        writer.writerow(["id", "nome", "idade", "sintoma", "nivel_urgencia", "tempo_espera_minutos"])
        # Escreve as linhas geradas
        writer.writerows(dados)
