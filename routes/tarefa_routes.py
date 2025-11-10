from flask import Blueprint, request, jsonify
from models.tarefa import Tarefa

tarefa_bp = Blueprint("tarefa_bp", __name__)

@tarefa_bp.route("/", methods=["GET"])
def listar():
    return jsonify(Tarefa.listar()), 200

@tarefa_bp.route("/", methods=["POST"])
def criar():
    try:
        print("Recebendo requisição POST para criar tarefa")
        dados = request.json
        print(f"Dados recebidos: {dados}")
        
        if not dados:
            print("Erro: Dados não fornecidos")
            return jsonify({"error": "Dados não fornecidos"}), 400
            
        # Validar campos obrigatórios
        campos_obrigatorios = ["titulo", "setor", "prioridade", "status", "responsavel"]
        for campo in campos_obrigatorios:
            if campo not in dados or not dados[campo]:
                print(f"Erro: Campo {campo} está faltando ou vazio")
                return jsonify({"error": f"Campo {campo} é obrigatório"}), 400

        print("Criando tarefa no banco de dados...")
        tarefa_id = Tarefa.criar(
            dados["titulo"],
            dados["setor"],
            dados["prioridade"],
            dados["status"],
            dados["responsavel"],
            dados.get("prazo_entrega")  # Usando get para campo opcional
        )
        
        print(f"Tarefa criada com sucesso! ID: {tarefa_id}")
        return jsonify({
            "message": "Tarefa criada com sucesso!",
            "id": tarefa_id
        }), 201
    except Exception as e:
        import traceback
        print(f"Erro ao criar tarefa: {str(e)}")
        print("Traceback completo:")
        print(traceback.format_exc())
        return jsonify({"error": f"Erro ao criar tarefa: {str(e)}"}), 500

@tarefa_bp.route("/<int:id>", methods=["PUT"])
def editar(id):
    dados = request.json
    Tarefa.editar(
        id,
        dados["titulo"],
        dados["setor"],
        dados["prioridade"],
        dados["status"],
        dados["responsavel"],
        dados["prazo_entrega"],
    )
    return jsonify({"message": "Atualizada!"}), 200

@tarefa_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    Tarefa.deletar(id)
    return jsonify({"message": "Excluída!"}), 200
