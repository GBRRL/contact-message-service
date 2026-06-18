import requests

from config import ZAPI_INSTANCE_ID, ZAPI_TOKEN

def enviar_mensagem(telefone, mensagem):
    url = (
        f"https://api.z-api.io/instances/"
        f"{ZAPI_INSTANCE_ID}/token/"
        f"{ZAPI_TOKEN}/send-text"
    
    )

    dados = {
        "phone": telefone,
        "message": mensagem
    
    }
    response = requests.post(url, json=dados)
    
    print(response.status_code)
    print(response.text)