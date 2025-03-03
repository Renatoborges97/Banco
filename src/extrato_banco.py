
def exibir_extrato(saldo,/, *, extrato):
    print("\n======== EXTRATO ========")
    print("Não foram Realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print("===========================")