from database import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario:
    @staticmethod
    def criar(email, senha, nome):
        conexao = get_connection()
        cursor = conexao.cursor()

        try:
            # Hash da senha antes de salvar
            senha_hash = generate_password_hash(senha)
            
            cursor.execute("""
                INSERT INTO usuarios (email, senha, nome)
                VALUES (%s, %s, %s)
            """, (email, senha_hash, nome))
            
            conexao.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erro ao criar usuário: {str(e)}")
            conexao.rollback()
            raise e
        finally:
            conexao.close()

    @staticmethod
    def verificar_login(email, senha):
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        try:
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            usuario = cursor.fetchone()
            
            if usuario and check_password_hash(usuario['senha'], senha):
                # Remove a senha do objeto antes de retornar
                del usuario['senha']
                return usuario
            return None
        except Exception as e:
            print(f"Erro ao verificar login: {str(e)}")
            return None
        finally:
            conexao.close()

    @staticmethod
    def buscar_por_email(email):
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        try:
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            usuario = cursor.fetchone()
            if usuario:
                del usuario['senha']
            return usuario
        finally:
            conexao.close()