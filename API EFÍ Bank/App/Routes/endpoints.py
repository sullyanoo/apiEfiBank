# Configurações para autenticação
CLIENT_ID = "YOUR-CLIENT-ID"  # Substitua com seu client_id real
CLIENT_SECRET = "YOUR-CLIENT-SECRET"  # Substitua com seu client_secret real
CERTIFICADO = './certificado.pem'  # Caminho para o certificado .pem

URL_BASE_H = "https://pix-h.api.efipay.com.br"
URL_BASE_P = "https://pix.api.efipay.com.br"

# URL da API de autenticação
AUTH_URL_H = URL_BASE_H + "/oauth/token"  # Para ambiente de Desenvolvimento Homologação 
AUTH_URL_P = URL_BASE_P + "/oauth/token" # Para ambiente de Desenvolvimento Produção

# URL da API de cobrança imediata
URL_COBIMEDIATA_H = URL_BASE_H + "/v2/cob"
URL_COBIMEDIATA_P = URL_BASE_P + "/v2/cob"

# URL da API de cobranças com vencimento
URL_COBVENCIMENTO_H = URL_BASE_H + "/v2/cobv"
URL_COBVENCIMENTO_P = URL_BASE_P + "/v2/cobv"

# URL da API de gestão de pix
URL_GESTPIX_H = URL_BASE_H + "/v2/pix"
URL_GESTPIX_P = URL_BASE_P + "/v2/pix"

# URL da API de Payloads Location
URL_PAYLOCATIONS_H = URL_BASE_H + "/v2/loc"
URL_PAYLOCATIONS_P = URL_BASE_P + "/v2/loc"

# URL da API para cobranças em lote
URL_COBLOTE_H = URL_BASE_H + "/v2/lotecobv"
URL_COBLOTE_P = URL_BASE_P + "/v2/lotecobv"

