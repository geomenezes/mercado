from tools import cadastra_cliente, cadastra_produto, cadastra_venda, alimenta_estoque

print("===============================================================")

print("===================== Mercado da Geovanna =====================")

print("===============================================================")

print("============================ Menu =============================")

print("======================= Digite uma opção ======================")

escolha = int(input("""
       Para cadastrar cliente, digite: 1
       Para cadastrar produto, digite: 2
       Para consultar estoque, digite: 3
       Para alimentar estoque, digite: 4
       Para fazer uma venda, digite: 5
       Para sair do mercado, digite: 6
       Para voltar ao menu, digite: 0
       
       Sua escolha: """))

while escolha:

    if escolha == 1:
        print("Você escolheu cadastrar o cliente!")
        nome = str(input("Digite o nome do seu cliente: "))
        cpf = str(input(f"Digite o CPF de {nome}: "))
        cadastra_cliente(nome, cpf)
        
        opcao = input("Deseja cadastar outro cliente? sim / nao")
        if opcao == "sim":
            pass
        if opcao == "nao":
            pass
        else:
            print("Digite uma opção válida!")
        
        break
    
    if escolha == 2:
        pass

    if escolha == 3:
        pass

    if escolha == 4:
        pass

    if escolha == 5:
        pass

    if escolha == 6:
        pass

    if escolha == 0:
        pass

