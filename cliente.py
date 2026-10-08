"""Classe Cliente."""


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"
