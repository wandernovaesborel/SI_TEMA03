from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Dicionário de respostas associadas a palavras-chave
respostas = {
    "Olá! Como posso ajudar?": ["ola", "oi", "olá"],
    "Seu pedido foi recebido!": ["pedido", "fazer pedido", "comprar"],
    "Caneta: 10\nCaderno: 20\nBorracha: 15": ["estoque", "disponibilidade"]
}

# Resposta padrão
resposta_padrao = "Desculpe, não entendi. Pode repetir?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensagem = request.form["mensagem"].lower()

    # Verificar se a mensagem corresponde a alguma pergunta conhecida
    for resposta, palavras_chave in respostas.items():
        if any(palavra_chave in mensagem for palavra_chave in palavras_chave):
            # Se sim, retornar a resposta correspondente
            return resposta
    
    # Se nenhuma pergunta for correspondida, retornar a resposta padrão
    return resposta_padrao

if __name__ == "__main__":
    app.run(debug=True)
