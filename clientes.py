
class Cliente:
    def __init__(self, nome=str, cpf=str):
        self.nome = nome
        self.cpf = cpf
    
cliente1 = Cliente("fulano de tal", "7578575")    
print(cliente1.nome)