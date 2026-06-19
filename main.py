from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem

def gerar_mensagem(nome):
    return f"Olá, {nome} tudo bem com você?"

def processar_contato(contato):
    telefone = contato["telefone"]
    nome = contato["nome"]
    
    mensagem = gerar_mensagem(nome)

    print(f"\nEnviando mensagem para {nome}...")
    enviar_mensagem(telefone, mensagem)

def main():
    contatos = buscar_contatos()

    for contato in contatos:
        processar_contato(contato)


main()