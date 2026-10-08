"""Menu de terminal do sistema bancário."""

from banco import Banco
from conta import SaldoInsuficienteError

MENU = """
===== SISTEMA BANCÁRIO =====
1 - Cadastrar cliente
2 - Abrir conta
3 - Depositar
4 - Sacar
5 - Transferir
6 - Consultar saldo
0 - Sair
"""


def ler_numero(texto, tipo=float):
    try:
        return tipo(input(texto).replace(",", "."))
    except ValueError:
        raise ValueError("Entrada numérica inválida.")


def executar(banco, opcao):
    if opcao == "1":
        cliente = banco.cadastrar_cliente(input("Nome: "), input("CPF: "))
        print(f"Cliente cadastrado: {cliente}")
    elif opcao == "2":
        cpf = input("CPF do cliente: ")
        tipo = input("Tipo (1 - Corrente, 2 - Poupança): ")
        print("Conta aberta:", banco.abrir_conta(cpf, tipo))
    elif opcao == "3":
        conta = banco.buscar_conta(ler_numero("Nº da conta: ", int))
        conta.depositar(ler_numero("Valor: "))
        print("Depósito realizado.", conta)
    elif opcao == "4":
        conta = banco.buscar_conta(ler_numero("Nº da conta: ", int))
        conta.sacar(ler_numero("Valor: "))
        print("Saque realizado.", conta)
    elif opcao == "5":
        origem = banco.buscar_conta(ler_numero("Conta de origem: ", int))
        destino = banco.buscar_conta(ler_numero("Conta de destino: ", int))
        origem.transferir(destino, ler_numero("Valor: "))
        print("Transferência realizada.")
    elif opcao == "6":
        print(banco.buscar_conta(ler_numero("Nº da conta: ", int)))
    else:
        print("Opção inválida.")


def main():
    banco = Banco()
    while True:
        print(MENU)
        opcao = input("Escolha: ").strip()
        if opcao == "0":
            print("Encerrando.")
            break
        try:
            executar(banco, opcao)
        except (ValueError, SaldoInsuficienteError) as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
