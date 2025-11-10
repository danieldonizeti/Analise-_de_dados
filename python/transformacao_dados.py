import pandas as pd
import os

# Caminhos
caminho_entrada = "dados/produtividade.csv"
caminho_saida = "dados/produtividade_tratada.csv"

# Lê o CSV original
df = pd.read_csv(caminho_entrada)

print("Pré-visualização dos dados originais:\n")
print(df.head())

# --- Limpeza e padronização ---
# 1. Padronizar nomes das colunas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 2. Se houver colunas parecidas com 'produtividade', manter apenas uma
colunas_produtividade = [c for c in df.columns if "produtivid" in c]
if len(colunas_produtividade) > 1:
    print(f"Removendo colunas duplicadas: {colunas_produtividade[1:]}")
    df = df.drop(columns=colunas_produtividade[1:])

# 3. Garantir tipo numérico
df["produtividade_ton_hect"] = pd.to_numeric(df["produtividade_ton_hect"], errors="coerce")

# 4. Criar categoria de produtividade
df["categoria_produtividade"] = pd.cut(
    df["produtividade_ton_hect"],
    bins=[0, 20, 30, 40, 50],
    labels=["Baixa", "Média", "Alta", "Excelente"]
)

# --- Exportação ---
os.makedirs("../dados", exist_ok=True)
df.to_csv(caminho_saida, index=False)

print("\n✅ Dados tratados com sucesso!")
print(f"Arquivo salvo em: {caminho_saida}")
print("\nPrévia final:\n", df)
