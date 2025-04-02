try:
    # Realizando conexão com o banco de dados
    db = SQLDatabase.from_uri('sqlite:///db.sqlite3')

    # Tentando realizar uma consulta simples
    with db.engine.connect() as connection:
        result = connection.execute("SELECT 1")  # Verifica se é possível executar um comando simples
        print("Conexão com o banco de dados foi realizada com sucesso!")
except Exception as e:
    print("Conexão com o banco de dados não foi realizada.")
    print(f"Erro: {e}")