# Contact Message Service

Projeto desenvolvido em Python com o objetivo de automatizar o envio de mensagens via WhatsApp.

A aplicação utiliza o Supabase para armazenar os contatos e a Z-API para realizar o envio das mensagens, permitindo centralizar e automatizar o processo de comunicação.

## Setup da tabela

Crie uma tabela chamada contatos com os seguintes campos:

- id
- nome
- telefone

## Instalação

Clone o repositório:
git clone <url-do-repositorio>

Acesse a pasta do projeto:
cd contact-message-service

Instale as dependências:
pip install -r requirements.txt

## Configuração do ambiente

Crie um arquivo .env com as seguintes variáveis:

SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=


## Execução

Execute a aplicação com:
python main.py

## Tecnologias utilizadas

* Python
* Supabase
* Z-API
* Requests







