import textwrap
import deposito 
import extrato_banco

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

        elif opcao == 'e':
            extrato_banco.exibir_extrato(saldo, extrato=extrato)

main()

