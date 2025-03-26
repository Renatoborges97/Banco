import textwrap
import deposito 
import extrato_banco
import saque
import novo_usuario
import nova_conta

def menu():
    menu = """\n
    ================================= MENU =================================
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Conta
    [nu]\t Novo Usuário
    [q]\t Sair
    \n
    => """

    return input(textwrap.dedent(menu))

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 1500
    extrato = ""
    numero_saque = 0
    usuario = []
    conta = []

    while True: 
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = deposito.depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Digite o valor do Saque: "))

            saldo, extrato, numero_saque = saque.sacar (
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUE
            )

        elif opcao == 'e':
            extrato_banco.exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nc':
            conta = nova_conta.criar_conta(usuario, conta, AGENCIA)

        elif opcao == 'nu':
            usuario = novo_usuario.criar_usuario(usuario)

main()

