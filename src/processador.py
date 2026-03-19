import csv
from typing import List, Dict, Any

def processar_dados_csv(caminho_arquivo: str = "dados/pacientes_raw.csv") -> List[Dict[str, Any]]:
    """
    Lê o CSV, aplica regras de validação (idade > 0, urgência e tempo não nulos) e
    retorna apenas as linhas válidas já estruturadas em dicionários.
    """
    dados_limpos = []
    
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        # csv.DictReader ajuda usando os cabeçalhos como chaves do dicionário
        leitor_csv = csv.DictReader(arquivo)
        
        for linha in leitor_csv:
            try:
                # Regras de negócio de limpeza: ignorar vazio/nulo onde não deve
                urgencia_str = linha["nivel_urgencia"].strip()
                tempo_str = linha["tempo_espera_minutos"].strip()
                
                # Descartar vazios
                if not urgencia_str or not tempo_str:
                    continue
                
                # Conversão e verificação numérica
                idade = int(linha["idade"])
                # Descartar idades negativas
                if idade < 0:
                    continue
                
                id_paciente = int(linha["id"])
                urgencia = int(urgencia_str)
                tempo = int(tempo_str)
                sintoma = linha["sintoma"].strip()
                nome = linha["nome"].strip()
                
                # Uma vez validado, montar o registro final
                dado_valido = {
                    "id": id_paciente,
                    "nome": nome,
                    "idade": idade,
                    "sintoma": sintoma,
                    "nivel_urgencia": urgencia,
                    "tempo_espera_minutos": tempo
                }
                
                dados_limpos.append(dado_valido)
                
            except (ValueError, KeyError):
                # Caso haja qualquer corrupção séria que quebre o cast de tipo, a linha é engolida/descartada.
                continue
                
    return dados_limpos
