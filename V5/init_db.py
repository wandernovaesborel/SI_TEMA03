import sqlite3

DB_PATH = "estoque.db"

def inicializar_bd():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Criação da tabela para perguntas e respostas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS perguntas_respostas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT NOT NULL,
            resposta TEXT NOT NULL
        )
    """)

    # Inserindo dados iniciais na tabela perguntas_respostas
    perguntas_iniciais = [
        ("quantos lápis tem no estoque?", "Temos 50 lápis no estoque."),
        ("qual o preço da borracha?", "A borracha custa R$2,00."),
        ("quais produtos estão disponíveis?", "Temos lápis, borracha, canetas e cadernos.")
    ]
    cursor.executemany("""
        INSERT INTO perguntas_respostas (pergunta, resposta)
        VALUES (?, ?)
    """, perguntas_iniciais)

    # Criação da tabela estoque
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            classificacao TEXT NOT NULL,
            item TEXT NOT NULL,
            quantidade_minima INTEGER NOT NULL,
            quantidade_real INTEGER NOT NULL,
            valor REAL NOT NULL
        )
    """)

    # Inserindo dados iniciais na tabela estoque
    estoque_inicial = [
        ("Eletrônicos", "Celular", 5, 10, 1500.00),
        ("Eletrodomésticos", "Geladeira", 3, 4, 2500.00),
        ("Móveis", "Sofá", 2, 5, 2000.00),
        ("Eletrônicos", "Notebook", 2, 8, 3500.00),
        ("Móveis", "Mesa", 1, 3, 700.00),
        ("Eletrodomésticos", "Micro-ondas", 3, 2, 400.00)
    ]
    cursor.executemany("""
        INSERT INTO estoque (classificacao, item, quantidade_minima, quantidade_real, valor)
        VALUES (?, ?, ?, ?, ?)
    """, estoque_inicial)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    inicializar_bd()
    print("Banco de dados inicializado com sucesso!")
