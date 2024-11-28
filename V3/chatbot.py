from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Definindo as saudações
saudacoes_usuario = ["oi", "olá", "eae", "opa"]
saudacoes_bot = ["Olá! Vi que você está interessado no Produto X. Quer fazer um orçamento rápido?",
                 "Olá! Estou aqui para te ajudar a fazer um orçamento do Produto X. Vamos começar?"]

# Variáveis de controle de fluxo
passo = 0
nome = ""
telefone = ""
email = ""

# Dicionário de opções de escolha para cada etapa do fluxo
opcoes_fluxo = {
    1: ["SIM", "NÃO"],
    3: ["E-MAIL", "WHATSAPP"]
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    global passo, nome, telefone, email

    mensagem = request.form['mensagem'].lower()
    passo = int(request.form['passo'])

    if mensagem in saudacoes_usuario:
        resposta_bot = random.choice(saudacoes_bot)
        passo = 1
    elif passo == 1:
        if mensagem == "sim":
            resposta_bot = "Primeiro, me diga seu nome, telefone e e-mail!"
            passo = 2
        else:
            resposta_bot = "Ok, se precisar estou por aqui!"
            passo = 0
    elif passo == 2:
        nome, telefone, email = extract_info(mensagem)
        resposta_bot = "Obrigado. Você prefere fazer o orçamento por e-mail ou WhatsApp?"
        passo = 3
    elif passo == 3:
        if mensagem == "e-mail":
            resposta_bot = f"Obrigado, {nome}. Enviaremos o orçamento para o seu e-mail: {email}."
            passo = 0
        elif mensagem == "whatsapp":
            resposta_bot = f"Obrigado, {nome}. Clique no link para ser redirecionado."
            passo = 0
        else:
            resposta_bot = "Por favor, escolha entre 'e-mail' ou 'WhatsApp'."
    else:
        resposta_bot = "Desculpe, eu não entendi. Poderia repetir, por favor?"

    # Adiciona opções de escolha específicas para esta etapa do fluxo
    if passo in opcoes_fluxo:
        resposta_bot += " [" + ", ".join(opcoes_fluxo[passo]) + "]"

    return resposta_bot

def extract_info(mensagem):
    partes = mensagem.split()
    nome = partes[0]
    telefone = partes[1]
    email = partes[2]
    return nome, telefone, email

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
