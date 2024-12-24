from flask import Flask, request, jsonify
import core

app = Flask(__name__)

# -------------------------------------------- Certification -------------------------------------------------------------------------------
@app.route('/api/para_efibank', methods=['POST'])
def api_para_efibank():
    dados = request.json
    if not dados:
        return jsonify({"message": "Dados não fornecidos"}), 400

    # Obter o token de autenticação
    token, erro = core.obter_token()
    if not token:
        return jsonify({"error": erro}), 400

    # Enviar os dados para a API do EFí Bank
    response, status_code = core.enviar_para_efibank(dados, token)

    return jsonify(response), status_code

# -------------------------------------------- Payments ------------------------------------------------------------------------------------

@app.route('/api/para_efibank/<int:id>', methods=['GET'])
def api_get_cobranca_imediata(id):
    dados = request.json
    if not dados:
        return jsonify({"message": "Dados não fornecidos"}), 400

    # Obter o token de autenticação
    token, erro = core.obter_token()
    if not token:
        return jsonify({"error": erro}), 400

    # Enviar os dados para a API do EFí Bank
    response, status_code = core.enviar_para_efibank(dados, token)

    return jsonify(response), status_code

if __name__ == '__main__':
    app.run(debug=True)
