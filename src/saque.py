def sacar(*, valor, extrato, limite, limite_saque, saldo, numero_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite 
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_saldo:
        print("\n@@ Operação falhou! Não tem saldo suficiente. @@")

    elif excedeu_limite:
        print("\n@@ Operação falhou! O valor do saque excedeu o limite. @@")

    elif excedeu_saque:
        print("\n@@ Operação falhou! O limite de saque foi foi atingido. @@")

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saque += 1
        print("\n === Saque Realizado com sucesso ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saque