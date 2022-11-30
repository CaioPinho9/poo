class FichaBancaria:

    def __init__(self):
        self.__numero = 0
        self.__nome = ''
        self.__cpf = ''
        self.__saldo = 0

    def get_numero(self):
        return self.__numero

    def get_nome(self):
        return self.__nome

    def get_saldo(self):
        return self.__saldo

    def get_cpf(self):
        return self.__cpf

    def set_numero(self, numero_conta):
        self.__numero = numero_conta

    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def debite(self, valor):
        self.__saldo -= valor

    def credite(self, valor):
        self.__saldo += valor