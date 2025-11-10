from database import get_connection

class Tarefa:

    @staticmethod
    def listar():
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tarefas")
        tarefas = cursor.fetchall()
        conexao.close()
        return tarefas

    @staticmethod
    def criar(titulo, setor, prioridade, status, responsavel, prazo_entrega):
        conexao = get_connection()
        cursor = conexao.cursor()

        try:
            cursor.execute("""
                INSERT INTO tarefas (titulo, setor, prioridade, status, responsavel, prazo_entrega)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (titulo, setor, prioridade, status, responsavel, prazo_entrega))
            
            conexao.commit()
            
            # Retornar o ID da tarefa criada
            return cursor.lastrowid
        except Exception as e:
            print(f"Erro ao criar tarefa: {str(e)}")
            conexao.rollback()
            raise e
        finally:
            conexao.close()

    @staticmethod
    def editar(id, titulo, setor, prioridade, status, responsavel, prazo_entrega):
        conexao = get_connection()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE tarefas
            SET titulo=%s, setor=%s, prioridade=%s, status=%s, responsavel=%s, prazo_entrega=%s
            WHERE id=%s
        """, (titulo, setor, prioridade, status, responsavel, prazo_entrega, id))

        conexao.commit()
        conexao.close()

    @staticmethod
    def deletar(id):
        conexao = get_connection()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id=%s", (id,))
        conexao.commit()
        conexao.close()
