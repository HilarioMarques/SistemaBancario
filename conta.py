"""Classes de conta bancária: encapsulamento, herança e polimorfismo."""


class SaldoInsuficienteError(Exception):
    """Lançada quando o saque excede o valor disponível."""


class Conta:
    tipo = "Conta"

    def __init__(self, numero, titular, saldo_inicial=0.0):
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")
        self._numero = numero
        self._titular = titular
        self._saldo = saldo_inicial

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @staticmethod
    def _validar_valor(valor):
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")

    def depositar(self, valor):
        self._validar_valor(valor)
        self._saldo += valor

    def sacar(self, valor):
        self._validar_valor(valor)
        if valor > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente. Disponível: R$ {self._saldo:.2f}"
            )
        self._saldo -= valor

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

    def __str__(self):
        return (f"[{self.tipo}] nº {self._numero} | "
                f"{self._titular.nome} | saldo: R$ {self._saldo:.2f}")


class ContaCorrente(Conta):
    tipo = "Conta Corrente"

    def __init__(self, numero, titular, saldo_inicial=0.0, limite=500.0):
        super().__init__(numero, titular, saldo_inicial)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        # Polimorfismo: permite usar o limite (cheque especial).
        self._validar_valor(valor)
        if valor > self._saldo + self._limite:
            disponivel = self._saldo + self._limite
            raise SaldoInsuficienteError(
                f"Limite excedido. Disponível com limite: R$ {disponivel:.2f}"
            )
        self._saldo -= valor


class ContaPoupanca(Conta):
    tipo = "Conta Poupança"

    def aplicar_rendimento(self, taxa=0.005):
        if taxa < 0:
            raise ValueError("A taxa não pode ser negativa.")
        self._saldo += self._saldo * taxa
