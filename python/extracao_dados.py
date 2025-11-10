import pandas as pd
import oracledb
import os

conn = oracledb.connect(
    user="hr",
    password="hr",
    dsn="localhost:1521/XEPDB1"
)

querry = """
SELECT f.nome_fazenda AS Fazenda, f.regiao_fazenda AS Região, c.nome_cultura AS Cultura,
       p.ano_safra AS Ano_safra, ROUND(p.quant_tonelada/ f.area_hectares, 2) AS Produtividade_Ton_Hect
FROM producao p
JOIN fazenda f ON p.id_fazenda = f.id_fazenda
JOIN cultura c ON p.id_cultura = c.id_cultura
ORDER BY Produtividade_Ton_Hect DESC
"""

#Carregando os dados pelo pandas
df = pd.read_sql(querry, conn)
conn.close()

print(df)

os.makedirs("../dados", exist_ok=True)
df.to_csv("dados/produtividade.csv", index=False, encoding='utf-8-sig')
print("✅ Dados exportados para 'dados/produtividade.csv'")
