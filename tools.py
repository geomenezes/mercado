import sqlite3

con = sqlite3.connect('mercado.db')


"""
Dica da geovaninha: integrar tabela de produtos com o estoque
incluir chave primaria e email em clientes 
atualizar estoque (update into estoque where (id))


cur = con.cursor()

# Create table 
cur.execute('''CREATE TABLE clientes
               (nome text, cpf text)''')

cur.execute('''CREATE TABLE produto
               (nome text, desc text, preco float)''')

cur.execute('''CREATE TABLE estoque
               (produto text, quantidade int, preco float)''')
               
cur.execute('''CREATE TABLE vendas
               (date text, cliente text, produto text, valor float, qtde int, total float)''')

# Insert a row of data
#cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

"""

#persistencia 


def alimenta_estoque(produto=str, quantidade=int, preco=float):
    connection = sqlite3.connect('mercado.db')
    cursor = connection.cursor()
    nome_prod = produto
    qtde = quantidade
    valor = preco
    try:
        cursor.execute("""
            INSERT INTO estoque (produto, quantidade, preco) VALUES (?,?,?) """, (nome_prod, qtde, valor))
    
        connection.commit()
        response = print("Seu estoque foi cadastrado com sucesso! ._.")
    
    except sqlite3.IntegrityError:
        print("Estoque não cadastrado")
        return False
    connection.close()
    
    return response 


def cadastra_cliente(nome=str, cpf=str):
    connection = sqlite3.connect('mercado.db')
    cursor = connection.cursor()
    name = nome
    documento = cpf
    try:
        cursor.execute("""
            INSERT INTO clientes (nome, cpf) VALUES (?,?) """, (name, documento))
    
        connection.commit()
        response = print("Seu cliente foi cadastrado com sucesso! ._.")
    
    except sqlite3.IntegrityError:
        print("Cliente não cadastrado")
        return False
    connection.close()
    
    return response 


def cadastra_produto(nome=str, desc=str, preco=float):
    connection = sqlite3.connect('mercado.db')
    cursor = connection.cursor()
    name = nome
    description = desc
    valor = preco
    try:
        cursor.execute("""
            INSERT INTO produto (nome, desc, preco) VALUES (?,?,?) """, (name, description, valor))
    
        connection.commit()
        response = print("Seu produto foi cadastrado com sucesso! ._.")
    
    except sqlite3.IntegrityError:
        print("Produto não cadastrado")
        return False
    connection.close()
    
    return response 


def cadastra_venda(date=str, cliente=str, produto=str, valor=float, qtde=int, total=float):
    connection = sqlite3.connect('mercado.db')
    cursor = connection.cursor()
    data = date
    nome = cliente
    prod = produto
    preco = valor
    quant = qtde
    total_venda = total
    preco = valor
    try:
        cursor.execute("""
            INSERT INTO produto (data, cliente, produto, valor, qtde, total) VALUES (?,?,?,?,?,?) """, (data, nome, prod, preco, quant, total_venda))
    
        connection.commit()
        response = print("Sua venda foi registrada com sucesso! ._.")
    
    except sqlite3.IntegrityError:
        print("Venda não registrada")
        return False
    connection.close()
    
    return response 



#cadastra_produto("Playstation 5", "Console da Sony", 2500)
#cadastra_cliente("Playstation 5", "2500")
#alimenta_estoque("Playstation 5", 5, 2500)
#cadastra_venda("Playstation 5", "Console da Sony", 2500)