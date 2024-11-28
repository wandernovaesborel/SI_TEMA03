from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Caminho do banco de dados SQLite
DB_PATH = "estoque.db"

# Função para buscar resposta no banco de dados
def buscar_resposta(mensagem):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Busca resposta correspondente à pergunta
    cursor.execute("""
        SELECT resposta 
        FROM perguntas_respostas 
        WHERE LOWER(pergunta) = ?
        LIMIT 1
    """, (mensagem.lower(),))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return resultado[0]
    return "Desculpe, não entendi. Você pode me ensinar uma nova resposta?"

# Função para adicionar nova pergunta e resposta
def adicionar_pergunta_resposta(pergunta, resposta):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO perguntas_respostas (pergunta, resposta) 
        VALUES (?, ?)
    """, (pergunta.lower(), resposta))
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensagem = request.form["mensagem"]
    resposta = buscar_resposta(mensagem)
    return resposta

@app.route("/treinar", methods=["POST"])
def treinar():
    dados = request.json
    pergunta = dados.get("pergunta")
    resposta = dados.get("resposta")

    if not pergunta or not resposta:
        return jsonify({"status": "erro", "mensagem": "Pergunta e resposta são obrigatórias!"}), 400

    adicionar_pergunta_resposta(pergunta, resposta)
    return jsonify({"status": "sucesso", "mensagem": "Nova pergunta e resposta adicionadas com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
