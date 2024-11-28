import sqlite3

DB_PATH = "estoque.db"

def atualizar_perguntas_respostas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Apagar todas as perguntas e respostas existentes
    cursor.execute("DELETE FROM perguntas_respostas")
    
    # Inserir novas perguntas e respostas
    perguntas_respostas_novas = [
        ("Quais são as classificações disponíveis no estoque?", "As classificações disponíveis são: Eletrônicos, Eletrodomésticos, Móveis."),
        ("Qual a quantidade mínima do Celular?", "A quantidade mínima do item Celular é 5."),
        ("Qual o valor do Notebook?", "O valor do item Notebook é R$ 3500.00."),
        ("Qual a quantidade real da Geladeira?", "A quantidade real do item Geladeira é 4."),
        ("Qual o valor do Sofá?", "O valor do item Sofá é R$ 2000.00."),
        ("Qual a quantidade mínima do Micro-ondas?", "A quantidade mínima do item Micro-ondas é 3."),
        ("Quais são as classificações de itens disponíveis?", "As classificações disponíveis são: Eletrônicos, Eletrodomésticos, Móveis."),
        ("Qual a quantidade real da Mesa?", "A quantidade real do item Mesa é 3."),
        ("Qual o valor do item Micro-ondas?", "O valor do item Micro-ondas é R$ 400.00."),
        ("Qual a quantidade mínima do Sofá?", "A quantidade mínima do item Sofá é 2."),
        ("Quais itens têm quantidade mínima de 3?", "Os itens com quantidade mínima de 3 são: Geladeira, Micro-ondas."),
        ("Qual a quantidade real do Notebook?", "A quantidade real do item Notebook é 8."),
        ("Qual a quantidade mínima da Mesa?", "A quantidade mínima do item Mesa é 1."),
        ("Quais itens são da classificação Eletrônicos?", "Os itens da classificação Eletrônicos são: Celular, Notebook."),
        ("Qual a quantidade real do item Sofá?", "A quantidade real do item Sofá é 5."),
        ("Qual o valor da Geladeira?", "O valor do item Geladeira é R$ 2500.00."),
        ("Quais itens são da classificação Móveis?", "Os itens da classificação Móveis são: Sofá, Mesa.")
    ]
    
    # Inserir as novas perguntas e respostas
    cursor.executemany("""
        INSERT INTO perguntas_respostas (pergunta, resposta)
        VALUES (?, ?)
    """, perguntas_respostas_novas)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    atualizar_perguntas_respostas()
    print("Perguntas e respostas atualizadas com sucesso!")
