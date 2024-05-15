from flask import Flask, request, jsonify

from src.repositories.usuario_repository import consultar_por_email, inserir, deletar_por_email, atualizar

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/usuario")
def consultar_por_email_api():
    email = request.args.get('email')
    usuario = consultar_por_email(email)

    if usuario is None:
        return jsonify({"message": f"Usuario com email={email} nao encontrado"}), 404

    return jsonify(usuario)


@app.route('/usuario', methods=['POST'])
def inserir_usuario_api():
    usuario = request.get_json()
    inserir(usuario)
    return '', 204


@app.route('/usuario', methods=['PUT'])
def atualizar_usuario_api():
    usuario = request.get_json()
    atualizar(usuario)
    return '', 204


@app.route("/usuario", methods=['DELETE'])
def deletar_por_email_api():
    email = request.args.get('email')
    usuario = deletar_por_email(email)
    return jsonify(usuario)
