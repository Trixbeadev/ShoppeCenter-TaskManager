from database import get_connection

def check_database():
    try:
        # Tentar conectar ao banco
        conn = get_connection()
        cursor = conn.cursor()
        
        # Verificar se a tabela existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo VARCHAR(100) NOT NULL,
                setor VARCHAR(50) NOT NULL,
                prioridade VARCHAR(20) NOT NULL,
                status VARCHAR(20) NOT NULL,
                responsavel VARCHAR(100) NOT NULL,
                prazo_entrega DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        print("Banco de dados e tabela verificados com sucesso!")
        
    except Exception as e:
        print(f"Erro ao verificar banco de dados: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    check_database()