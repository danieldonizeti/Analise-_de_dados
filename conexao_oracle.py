import oracledb

connection = oracledb.connect(
    user="HR",
    password="hr",
    dsn="localhost:1521/XEPDB1"
)

print("✅ Conexão bem-sucedida!")
connection.close()
