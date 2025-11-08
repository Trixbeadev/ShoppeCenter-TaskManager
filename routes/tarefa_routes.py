from flask import Blueprint, request, jsonify
from models.tarefa import Tarefa

tarefa_bp = Blueprint("tarefas", __name__)

@tarefa_bp.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.json
    Tarefa.criar(
        dados["titulo"],
        dados["setor"],
        dados["prioridade"],
        dados["status"],
        dados["responsavel"],
        dados["prazo_entrega"]
    )
    return jsonify({"message": "Tarefa criada com sucesso!"}), 201


@tarefa_bp.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(Tarefa.listar())

