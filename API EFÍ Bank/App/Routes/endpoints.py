# encoding: utf-8

class Constants(object):
    APIS = {
        'CHARGES': {
            'URL': {
                'production': 'https://cobrancas.api.efipay.com.br/v1',
                'sandbox': 'https://cobrancas-h.api.efipay.com.br/v1'
            },
            'ENDPOINTS': {
                'authorize': {
                    'route': '/authorize',
                    'method': 'post'
                },
                'create_charge': {
                    'route': '/charge',
                    'method': 'post'
                },
                'create_one_step_charge': {
                    'route': '/charge/one-step',
                    'method': 'post'
                },
                'detail_charge': {
                    'route': '/charge/:id',
                    'method': 'get'
                },
                'update_charge_metadata': {
                    'route': '/charge/:id/metadata',
                    'method': 'put'
                },
                'update_billet': {
                    'route': '/charge/:id/billet',
                    'method': 'put'
                },
                'define_pay_method': {
                    'route': '/charge/:id/pay',
                    'method': 'post'
                },
                'cancel_charge': {
                    'route': '/charge/:id/cancel',
                    'method': 'put'
                },
                # Adicione os outros endpoints conforme necessário
            }
        },
        'PIX': {
            'URL': {
                'production': 'https://pix.api.efipay.com.br',
                'sandbox': 'https://pix-h.api.efipay.com.br'
            },
            'ENDPOINTS': {
                'authorize': {
                    'route': '/oauth/token',
                    'method': 'post'
                },
                'pix_create_charge': {
                    'route': '/v2/cob/:txid',
                    'method': 'put'
                },
                'pix_detail_charge': {
                    'route': '/v2/cob/:txid',
                    'method': 'get'
                },
                'pix_list_charges': {
                    'route': '/v2/cob',
                    'method': 'get'
                },
                # Adicione os outros endpoints conforme necessário
            }
        },
        'OPEN-FINANCE': {
            'URL': {
                'production': 'https://openfinance.api.efipay.com.br/v1',
                'sandbox': 'https://openfinance-h.api.efipay.com.br/v1'
            },
            'ENDPOINTS': {
                'authorize': {
                    'route': '/oauth/token',
                    'method': 'post'
                },
                'of_list_participants': {
                    'route': '/participantes/',
                    'method': 'get'
                },
                # Adicione os outros endpoints conforme necessário
            }
        },
        'PAYMENTS': {
            'URL': {
                'production': 'https://pagarcontas.api.efipay.com.br/v1',
                'sandbox': ''
            },
            'ENDPOINTS': {
                'authorize': {
                    'route': '/oauth/token',
                    'method': 'post'
                },
                'pay_request_bar_code': {
                    'route': '/codBarras/:codBarras',
                    'method': 'post'
                },
                'pay_list_payments': {
                    'route': '/resumo',
                    'method': 'get'
                },
                # Adicione os outros endpoints conforme necessário
            }
        },
        # Adicione as outras APIs conforme necessário
    }
