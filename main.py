from openai import OpenAI
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()
cliente = OpenAI()
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
        "Pedicure Masculina": "30min – R$ 38",
        "Remoção de Barba": "30min – R$ 60",
        "Revitalização Facial": "1h – R$ 99"
    }
}

def assistente_barbearia(pergunta):
    prompt_sistema = f"""
    Você é o assistente virtual da barbearia {barbearia_info['nome']}, localizada em {barbearia_info['endereco']}.
    Seu proprietário é {barbearia_info['proprietario']}.
    
    Ao iniciar uma interação, apresente-se como o assistente da barbearia e informe que pode ajudar com serviços, valores, localização e horário de funcionamento.
    
    Serviços oferecidos e preços:
    {', '.join([f'{s}: {barbearia_info['servicos'][s]}' for s in barbearia_info['servicos']])}.
    
    O telefone para contato é {barbearia_info['contato']} e o horário de funcionamento é {barbearia_info['horario']}.
    """
    
    resposta = cliente.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": pergunta}
        ],
        model=modelo,
        temperature=0.5,
        max_tokens=300,
        frequency_penalty=1.0
    )
    
    return f"Olá! Eu sou o assistente virtual da {barbearia_info['nome']}. Posso te ajudar com informações sobre serviços, valores, localização e mais!\n\n{resposta.choices[0].message.content}"

while True:
    pergunta = input("Digite sua pergunta sobre a barbearia (ou 'sair' para encerrar): ")
    if pergunta.lower() == "sair":
        break
    resposta = assistente_barbearia(pergunta)
    print(resposta)