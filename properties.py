import psycopg2
from psycopg2 import OperationalError

db_name = "livraria"
db_user = "postgres"
db_password = "1234"
db_host = "localhost" 
db_port = "5432"

try:
    # Estabelecer a conexão
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )

    cursor = conn.cursor()

    print("Conexão bem-sucedida!")


    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS usuarios (
    #         id SERIAL PRIMARY KEY,
    #         nome VARCHAR(100) NOT NULL
    #     );
    # """)
    # conn.commit()
    # print("Tabela 'usuarios' verificada/criada.")

    # # Exemplo: Inserir um novo registro
    # insert_sql = "INSERT INTO usuarios (nome) VALUES (%s);"
    # cursor.execute(insert_sql, ("Alice",))
    # conn.commit()
    # print("Novo usuário inserido.")



    # select_sql = "SELECT id, nome FROM usuarios;"
    # cursor.execute(select_sql)


    resultados = cursor.fetchall()

    print("\nResultados da tabela 'usuarios':")
    for row in resultados:
        print(f"ID: {row[0]}, Nome: {row[1]}")

except OperationalError as e:
    print(f"Ocorreu um erro de conexão: {e}")

finally:
    # Fechar o cursor e a conexão
    if 'conn' in locals() and conn:
        cursor.close()
        conn.close()
        print("\nConexão com o PostgreSQL fechada.")