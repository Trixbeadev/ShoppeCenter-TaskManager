import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3305,                  # <-- SUA PORTA
        user="root",               # <-- CONFIRME O USUÁRIO
        password="beasql",               # <-- SUA SENHA DO MYSQL (se tiver, coloque aqui)
        database="shoppecenter"    # <-- NOME DO BANCO
    )
