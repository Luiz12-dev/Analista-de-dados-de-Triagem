from src.gerador_dados import gerar_dados
from src.processador import processar_dados_csv
from src.banco_dados import inicializar_banco, salvar_dados_lote, exibir_relatorio_analitico

def main() -> None:
    print("="*60)
    print(" INICIANDO PIPELINE DE DADOS DA TRIAGEM (HEALTH-TECH) ")
    print("="*60)
    
    ARQUIVO_CSV = "dados/pacientes_raw.csv"
    BANCO_NOME = "triagem_database.db"
    QTD_REGISTROS = 50
  
    print("\n[Etapa 1/4] Gerando os dados brutos e ruidosos em CSV...")
    gerar_dados(caminho_arquivo=ARQUIVO_CSV, quantidade=QTD_REGISTROS)
    print(f" -> Arquivo criado mockado no caminho '{ARQUIVO_CSV}' ({QTD_REGISTROS} registros).")
    

    print("\n[Etapa 2/4] Lendo CSV e aplicando as regras de validação...")
    dados_limpos = processar_dados_csv(caminho_arquivo=ARQUIVO_CSV)
    print(f" -> Processamento concluído. {len(dados_limpos)} de {QTD_REGISTROS} pacientes passaram na validação.")
    
  
    print("\n[Etapa 3/4] Inicializando banco SQLite local e persistindo...")
    inicializar_banco(nome_banco=BANCO_NOME)
    salvar_dados_lote(dados=dados_limpos, nome_banco=BANCO_NOME)
    print(f" -> Tabela SQLite resetada, INSERT em batch realizado com segurança.")
    
    print("\n[Etapa 4/4] Executando análise em SQL no SQLite...")
    exibir_relatorio_analitico(nome_banco=BANCO_NOME)
    
    print("\n[FIM] Execução de PoC concluída com sucesso.")
    print("="*60)


if __name__ == '__main__':
    main()
