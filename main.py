from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem


contatos = buscar_contatos()

for contato in contatos:
    telefone = contato["telefone"]
    nome = contato["nome"]

    mensagem = f"Olá, {nome} tudo bem com você?"

    print(f"\nEnviando mensagem para {nome}...")
    enviar_mensagem(telefone, mensagem)