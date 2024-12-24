import requests, base64
import Routes.endpoints as endpoints

# Função para obter o token de autenticação
def obter_token():
    # Cria a autenticação básica (client_id:client_secret em base64)
    auth = base64.b64encode(
        f"{endpoints.CLIENT_ID}:{endpoints.CLIENT_SECRET}".encode()).decode()
    headers = {
        'Authorization': f"Basic {auth}",
        'Content-Type': 'application/json'
    }
    # Payload para a requisição de token
    payload = '{"grant_type": "client_credentials"}'
    try:
        # Faz a requisição para obter o token
        response = requests.post(endpoints.AUTH_URL_H, 
                                 headers=headers, 
                                 data=payload, 
                                 cert=endpoints.CERTIFICADO)

        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            token = response.json().get('access_token')
            return token
        else:
            return None, f"Erro ao obter token: {response.text}"

    except requests.exceptions.RequestException as e:
        return None, f"Erro de requisição: {str(e)}"

# Função para fazer a requisição para a API do EFí Bank usando o token
def enviar_para_efibank(dados, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    try:
        # Envia os dados para a API do EFí Bank
        response = requests.post(endpoints.AUTH_URL_H, 
                                 json=dados, 
                                 headers=headers, 
                                 cert=endpoints.CERTIFICADO)

        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            return response.json()  # Retorna os dados recebidos do EFí Bank
        else:
            return {"error": f"Erro ao acessar a API do EFí Bank: {response.text}"}, response.status_code
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro de requisição: {str(e)}"}, 500