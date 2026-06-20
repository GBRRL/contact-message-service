# Contact Message Service

Projeto desenvolvido em Python com o objetivo de automatizar o envio de mensagens via WhatsApp.

A aplicação utiliza o Supabase para armazenar os contatos e a Z-API para realizar o envio das mensagens, automatizando o processo de comunicação.


## Configuração da tabela no Supabase

No Supabase, crie uma tabela chamada `contatos` com a seguinte estrutura:

| Campo    | Tipo   |
| -------- | ------ |
| id       | bigint |
| nome     | text   |
| telefone | text   |

O campo `id` pode ser configurado como chave primária e gerado automaticamente.

## Instalação

**Clone o repositório:**

```bash
git clone https://github.com/GBRRL/contact-message-service.git
```

**Acesse a pasta do projeto:**

```bash
cd contact-message-service
```

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

## Configuração do ambiente

Crie um arquivo `.env` com as seguintes variáveis:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=
```

Os valores das variáveis podem ser obtidos nas configurações do projeto no Supabase e nas configurações da instância criada na Z-API.

## Execução

**Execute a aplicação com:**

```bash
python main.py
```

## Tecnologias utilizadas

- Python
- Supabase
- Z-API
- Requests








