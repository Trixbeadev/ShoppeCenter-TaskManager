from flask import Flask, send_from_directory, session
from flask_cors import CORS
from routes.tarefa_routes import tarefa_bp
from routes.auth_routes import auth_bp
import os

# Configurar o Flask para servir arquivos estáticos
app = Flask(__name__)
app.debug = True
app.secret_key = 'sua_chave_secreta_aqui'  # Importante para a sessão

# Configurar CORS para permitir credenciais
CORS(app, supports_credentials=True)

# Diretório onde estão os arquivos do frontend
frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frontend')

# Rota para a página principal
@app.route('/')
def serve_index():
    return send_from_directory(frontend_dir, 'index.html')

# Rota para arquivos estáticos (CSS, JS, etc)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(frontend_dir, path)

# Registrar as rotas
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(tarefa_bp, url_prefix="/tarefas")

if __name__ == "__main__":
    print(f"Servidor iniciando em http://127.0.0.1:5000")
    print(f"Servindo arquivos do diretório: {frontend_dir}")
    app.run(host="127.0.0.1", port=5000)
