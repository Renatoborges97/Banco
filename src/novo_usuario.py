def criar_usuario(usuarios):
    cpf = input('Digite seu CPF(somente numeros) ')

    verificar_usuario = next((user for user in usuarios if user["cpf"] == cpf), None)

    if verificar_usuario:
        print('Erro: Já existe um usuário cadastrado com esse CPF')
        return usuarios
    
    nome = input('Digite o nome do completo: ')
    data_nascimento = input('Digite a data de nascimento (DD/MM/AAAA): ')
    endereco = input('Digite o seu endereço (logradouro, número - bairro - cidade/UF): ')

    novo_usuario = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print('Usuário cadastrado com sucesso!')

    return usuarios