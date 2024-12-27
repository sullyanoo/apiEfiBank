from flask import Flask, request, jsonify
from core import Endpoints

# Configuração inicial do Flask
app = Flask(__name__)

# Configurações do Endpoints
efi_config = {
    "client_id": "seu_client_id",
    "client_secret": "seu_client_secret",
    "certificate": "/caminho/para/certificado.pem",
    "sandbox": True,  # Use False para produção
    "api_type": "CHARGES"  # Ajuste o tipo de API conforme necessário
}

# Instância da API EFí Bank
efi_api = Endpoints(efi_config)

# ------------------------------ CHARGES ------------------------------

@app.route('/api/efibank/charge', methods=['POST'])
def criar_cobranca():
    dados = request.json
    if not dados:
        return jsonify({"message": "Dados não fornecidos"}), 400

    try:
        # Chama o endpoint 'create_charge' com os dados fornecidos
        response = efi_api.CHARGES.create_charge(body=dados)  # Chama a função diretamente
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/efibank/charge/one-step', methods=['POST'])
def criar_cobranca_uma_etapa():
    dados = request.json
    if not dados:
        return jsonify({"message": "Dados não fornecidos"}), 400

    try:
        # Chama o endpoint 'create_one_step_charge' com os dados fornecidos
        response = efi_api.CHARGES.create_one_step_charge(body=dados)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/efibank/charge/<int:id>', methods=['GET'])
def buscar_cobranca(id):
    try:
        # Chama o endpoint 'detail_charge' passando o ID como parâmetro
        response = efi_api.CHARGES.detail_charge(params={"id": id})
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/efibank/charge/<int:id>/metadata', methods=['PUT'])
def atualizar_metadata_cobranca(id):
    dados = request.json
    if not dados:
        return jsonify({"message": "Dados não fornecidos"}), 400

    try:
        # Chama o endpoint 'update_charge_metadata' passando o ID e os dados
        response = efi_api.CHARGES.update_charge_metadata(params={"id": id}, body=dados)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/efibank/charge/<int:id>/billet', methods=['PUT'])
def atualizar_boleto(id):
    dados = request.json
    if not dados:
        return jsonify({"message": "Dados não fornecidos"}), 400

    try:
        # Chama o endpoint 'update_billet' passando o ID e os dados
        response = efi_api.CHARGES.update_billet(params={"id": id}, body=dados)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/efibank/charge/<int:id>/pay', methods=['POST'])
def definir_metodo_pagamento(id):
    dados = request.json
    if not dados:
        return jsonify({"message": "Dados não fornecidos"}), 400

    try:
        # Chama o endpoint 'define_pay_method' passando o ID e os dados
        response = efi_api.CHARGES.define_pay_method(params={"id": id}, body=dados)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/efibank/charge/<int:id>/cancel', methods=['PUT'])
def cancelar_cobranca(id):
    try:
        # Chama o endpoint 'cancel_charge' passando o ID
        response = efi_api.CHARGES.cancel_charge(params={"id": id})
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------ PIX ------------------------------

@app.route('/api/efibank/pix/create-charge/<string:txid>', methods=['PUT'])
def criar_cobranca_pix(txid):
    """
    Endpoint para criar uma cobrança no PIX.
    """
    dados = request.json
    if not dados:
        return jsonify({"message": "Dados não fornecidos"}), 400

    try:
        response = efi_api.PIX.pix_create_charge(params={"txid": txid}, body=dados)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/efibank/pix/detail-charge/<string:txid>', methods=['GET'])
def buscar_cobranca_pix(txid):
    """
    Endpoint para buscar uma cobrança PIX pelo TXID.
    """
    try:
        response = efi_api.PIX.pix_detail_charge(params={"txid": txid})
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/efibank/pix/list-charges', methods=['GET'])
def listar_cobrancas_pix():
    """
    Endpoint para listar cobranças PIX.
    """
    try:
        response = efi_api.PIX.pix_list_charges()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------ OPEN-FINANCE ------------------------------

@app.route('/api/efibank/of/list-participants', methods=['GET'])
def listar_participantes_open_finance():
    """
    Endpoint para listar participantes no Open Finance.
    """
    try:
        response = efi_api.Open.Finance.of_list_participants()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------ PAYMENTS ------------------------------

@app.route('/api/efibank/payments/pay-barcode/<string:codBarras>', methods=['POST'])
def pagar_com_boleto(codBarras):
    """
    Endpoint para realizar pagamento com código de barras.
    """
    dados = request.json
    if not dados:
        return jsonify({"message": "Dados não fornecidos"}), 400

    try:
        response = efi_api.PAYMENTS.pay_request_bar_code(params={"codBarras": codBarras}, body=dados)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/efibank/payments/list-payments', methods=['GET'])
def listar_pagamentos():
    """
    Endpoint para listar pagamentos realizados.
    """
    try:
        response = efi_api.PAYMENTS.pay_list_payments()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# Você pode ajustar as outras rotas da mesma forma

if __name__ == '__main__':
    app.run(debug=True)
