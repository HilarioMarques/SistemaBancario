"""Classe Banco: gerencia clientes e contas (composição)."""

from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca


class Banco:
    TIPOS = {"1": ContaCorrente, "2": ContaPoupanca}

    def __init__(self):
        self._clientes = {}
        self._contas = {}
        self._proximo_numero = 1

    def cadastrar_cliente(self, nome, cpf):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        if cpf in self._clientes:
            raise ValueError("Já existe cliente com esse CPF.")
        cliente = Cliente(nome.strip(), cpf)
        self._clientes[cpf] = cliente
        return cliente

    def abrir_conta(self, cpf, tipo):
        if cpf not in self._clientes:
            raise ValueError("Cliente não encontrado.")
        if tipo not in self.TIPOS:
            raise ValueError("Tipo de conta inválido.")
        cliente = self._clientes[cpf]
        conta = self.TIPOS[tipo](self._proximo_numero, cliente)
        self._proximo_numero += 1
        self._contas[conta.numero] = conta
        cliente.adicionar_conta(conta)
        return conta

    def buscar_conta(self, numero):
        if numero not in self._contas:
            raise ValueError("Conta não encontrada.")
        return self._contas[numero]
