import os
import csv
import subprocess
import sys

# CONFIGURAÇÃO DE CAMINHOS
# Descobre as pastas do projeto de forma automática
RAIZ_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_SCRIPTS = os.path.join(RAIZ_PROJETO, "scripts")
PASTA_DADOS = os.path.join(RAIZ_PROJETO, "dados")

# MAPEAMENTO DOS ARQUIVOS
# Caminho exato dos scripts dos teus colegas e do dataset
SCRIPT_COLETA = os.path.join(PASTA_SCRIPTS, "coleta_dados.py")  
SCRIPT_TREINAMENTO = os.path.join(PASTA_SCRIPTS, "treinar_modelo.py")  
ARQUIVO_DATASET = os.path.join(PASTA_DADOS, "dataset.csv")
LETRAS_ESPERADAS = {"A", "E", "I", "O", "U"}


# VERIFICAÇÃO DE AMBIENTE
# Garante que o terminal está na pasta certa e com o venv ativo
def verificar_ambiente():
    print("--- PASSO 1: Validando Ambiente ---")
    
    if not os.path.exists(os.path.join(RAIZ_PROJETO, "requirements.txt")):
        print("Erro: Executa o main.py a partir da raiz do projeto.")
        return False
        
    if not (hasattr(sys, "real_prefix") or (sys.base_prefix != sys.prefix)):
        print("Erro: O ambiente virtual (venv) nao esta ativo.")
        return False

    print("Ambiente virtual ativo.")
    print(f"Raiz validada: {RAIZ_PROJETO}\n")
    return True


# EXECUÇÃO DE SCRIPTS ISOLADOS
# Executa um script Python externo e avisa se ele falhar
def rodar_script(caminho_script, descricao):
    print(f"--- Executando: {descricao} ---")
    if not os.path.exists(caminho_script):
        print(f"Erro: O arquivo '{caminho_script}' nao foi encontrado.")
        return False

    try:
        subprocess.run([sys.executable, caminho_script], check=True, text=True)
        print(f"{descricao} concluido com sucesso.\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Falha critica ao executar: {os.path.basename(caminho_script)}.")
        print(f"Erro tecnico: {e}\n")
        return False


# CONSISTÊNCIA DOS DADOS
# Checa se o arquivo dataset.csv foi criado e se tem conteúdo dentro
def validar_dados():
    print("--- Validando Consistencia dos Dados ---")
    
    if not os.path.exists(ARQUIVO_DATASET):
        print(f"Erro: O arquivo '{ARQUIVO_DATASET}' nao foi gerado.")
        return False
        
    if os.path.getsize(ARQUIVO_DATASET) == 0:
        print(f"Erro: O arquivo '{ARQUIVO_DATASET}' esta vazio.")
        return False

    with open(ARQUIVO_DATASET, newline="") as f:
        reader = csv.DictReader(f)
        labels_presentes = {row["label"] for row in reader if row.get("label")}
 
    faltando = LETRAS_ESPERADAS - labels_presentes
    if faltando:
        print(f"Erro: faltam exemplos das letras: {sorted(faltando)}")
        return False
        
    print(f"Arquivo '{os.path.basename(ARQUIVO_DATASET)}' validado com letras: {sorted(labels_presentes)}\n")
    return True


# FUNÇÃO PRINCIPAL (PIPELINE)
# Coordena todo o fluxo na ordem correta
def main():
    print("EXECUCAO PRINCIPAL E VALIDACAO - MEMBRO 3\n")

    # 1. Valida o ambiente
    if not verificar_ambiente():
        sys.exit(1)

    # 2. Executa a coleta (Membro 1)
    if not rodar_script(SCRIPT_COLETA, "Coleta de Dados (Membro 1)"):
        sys.exit(1)

    # 3. Valida o arquivo gerado
    if not validar_dados():
        sys.exit(1)

    # 4. Executa o treinamento (Membro 2)
    if not rodar_script(SCRIPT_TREINAMENTO, "Treinamento do Modelo (Membro 2)"):
        sys.exit(1)

    print("PIPELINE FINALIZADO COM SUCESSO.")


if __name__ == "__main__":
    main()
