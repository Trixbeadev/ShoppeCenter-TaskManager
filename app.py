from flask import Flask
from routes.tarefa_routes import tarefa_bp

app = Flask(__name__)
app.register_blueprint(tarefa_bp)

@app.route("/")
def home():
    return {"message": "API ShoppeCenter funcionando!"}

if __name__ == "__main__":
    app.run(debug=True)
