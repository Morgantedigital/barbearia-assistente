import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
cliente = OpenAI(api_key=api_key)
modelo = "gpt-4"

# Dados da Barbearia
barbearia_info = {
    "nome": "Turquesa Barber",
    "endereco": "Rua do Retiro, 18, Centro, Jundiaí, SP, CEP 13201-030",
    "proprietario": "Danilo Rocha",
    "contato": "(11) 91311-0880",
    "horario": "Segunda a sábado, das 9h às 19h",
    "servicos": {
        "Acabamento Pezinho": "20min – R$ 15",
        "Barba com Máquina": "1h – R$ 55",
        "Barba Modelada": "1h – R$ 55",
        "Barba Tradicional": "1h – R$ 55",
        "Barbaterapia": "1h – R$ 55",
        "Bigode com Máquina": "30min – R$ 30",
        "Cabelo e Barba": "2h – R$ 100",
        "Corte Freestyle": "1h 30min – R$ 70",
        "Corte Masculino": "1h – R$ 55",
        "Design de Sobrancelhas Masculino": "15min – R$ 15",
        "Manicure Masculina": "30min – R$ 38",
        "Manicure e Pedicure Masculina": "1h – R$ 76",
        "Pedicure Masculina": "30min – R$ 38"
    }
}

# Criando a interface com Streamlit
st.title(f"💈 Assistente Virtual - {barbearia_info['nome']}")

st.write("👋 Olá! Eu sou o assistente virtual da barbearia. Como posso te ajudar hoje?")

# Inicializa o histórico de mensagens
if "historico" not in st.session_state:
    st.session_state.historico = []

# Exibir mensagens anteriores
for msg in st.session_state.historico:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input do usuário
pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    # Adicionar a pergunta ao histórico
    st.session_state.historico.append({"role": "user", "content": pergunta})
    
    # Criar o prompt para o assistente
    prompt_sistema = f"""
    Você é o assistente virtual da barbearia {barbearia_info['nome']}, localizada em {barbearia_info['endereco']}.
    O proprietário é {barbearia_info['proprietario']}.
    Contato: {barbearia_info['contato']} | Horário: {barbearia_info['horario']}.
    Os serviços oferecidos são:
    {', '.join(barbearia_info['servicos'].keys())}.
    
    Responda educadamente às perguntas dos clientes de maneira objetiva.
    """

    resposta = cliente.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": pergunta}
        ]
    )

    resposta_texto = resposta.choices[0].message.content

    # Adicionar resposta ao histórico
    st.session_state.historico.append({"role": "assistant", "content": resposta_texto})

    # Exibir resposta no chat
    with st.chat_message("assistant"):
        st.markdown(resposta_texto)
