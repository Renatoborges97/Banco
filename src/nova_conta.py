def criar_conta(usuarios, contas, agencia):
    cpf = input('Digite seu CPF(somente numeros) ')

    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)

    if not usuario:
        print('Usuário não encontrado! Cadastre um usuário antes de criar uma conta.')
        return contas
    
    numero_conta = len(contas) + 1
    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "cpf": cpf
    }

    contas.append(nova_conta)

    print(f'\nConta criada com sucesso! Agência: {agencia} | Número da Conta: {numero_conta}')
    return contas
    