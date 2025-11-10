from flask import Blueprint, request, jsonify, session
from models.usuario import Usuario

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        dados = request.json
        if not dados or "email" not in dados or "senha" not in dados:
            return jsonify({"error": "Email e senha são obrigatórios"}), 400

        usuario = Usuario.verificar_login(dados["email"], dados["senha"])
        if usuario:
            session['usuario_id'] = usuario['id']
            session['usuario_nome'] = usuario['nome']
            return jsonify({
                "message": "Login realizado com sucesso",
                "usuario": usuario
            }), 200
        else:
            return jsonify({"error": "Email ou senha inválidos"}), 401

    except Exception as e:
        print(f"Erro no login: {str(e)}")
        return jsonify({"error": "Erro ao fazer login"}), 500

@auth_bp.route("/cadastro", methods=["POST"])
def cadastro():
    try:
        dados = request.json
        if not dados:
            return jsonify({"error": "Dados não fornecidos"}), 400

        # Validar campos obrigatórios
        campos = ["email", "senha", "nome"]
        for campo in campos:
            if campo not in dados:
                return jsonify({"error": f"Campo {campo} é obrigatório"}), 400

        # Verificar se email já existe
        if Usuario.buscar_por_email(dados["email"]):
            return jsonify({"error": "Email já cadastrado"}), 400

        # Criar novo usuário
        usuario_id = Usuario.criar(
            dados["email"],
            dados["senha"],
            dados["nome"]
        )

        return jsonify({
            "message": "Usuário cadastrado com sucesso",
            "id": usuario_id
        }), 201

    except Exception as e:
        print(f"Erro no cadastro: {str(e)}")
        return jsonify({"error": "Erro ao cadastrar usuário"}), 500

@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logout realizado com sucesso"}), 200

@auth_bp.route("/verificar", methods=["GET"])
def verificar_sessao():
    if 'usuario_id' in session:
        return jsonify({
            "logado": True,
            "usuario": {
                "id": session['usuario_id'],
                "nome": session['usuario_nome']
            }
        }), 200
    return jsonify({"logado": False}), 401