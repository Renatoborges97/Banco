menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500   
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Digite o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido! Digite um valor maior que zero.")

    elif opcao == 's':
        valor = float(input("Digite o valor do Saque: "))

        excedeu_saldo  = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif excedeu_limite:
            print("Limite de saque excedido!")

        elif excedeu_saque:
            print("Limite de saque excecido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido!")

       

    elif opcao == 'e':
        print("\n########### Extrato ###########")
        print("Não foram realizadas operações!" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("################################")

    elif opcao == 'q':        
        print("Sair")
        break

    else:
        print("Opção inválida, digite as opções válidas!")
    