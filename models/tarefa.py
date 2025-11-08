models/tarefa.py
git status







models/tarefa.py
git status






CTRL + X




from database import get_connection

class Tarefa:
    @staticmethod
    def criar(titulo, setor, prioridade, status, responsavel, prazo_entrega):
        conexao = get_connection()
        cursor = conexao.cursor()
        sql = """
        INSERT INTO tarefas (titulo, setor, prioridade, status, responsavel, prazo_entrega)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (titulo, setor, prioridade, status, responsavel, prazo_entrega)
        cursor.execute(sql, valores)
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tarefas")
        tarefas = cursor.fetchall()
        conexao.close()
        return tarefas

git add models/tarefa.py
git status

CTRL + X






