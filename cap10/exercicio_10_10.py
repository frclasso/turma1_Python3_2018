#!/usr/bin/env python3

# -*-coding:utf-8 -*-

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


# Modifique o arquivo contas.py das listagens

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print("CC N°%s Saldo: %10.2f" %
              (self.numero, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.numero)
        for o in self.operacoes:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n      Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            return Conta.saque(self, valor)


joao = Cliente("João", "5554-3322")
jose = Cliente("José", "1243-3321")

conta = Conta([joao, jose], 2341, 500)
conta.resumo()
print(conta.saque(1000))
print(conta.saque(100))
conta.resumo()

conta2 = ContaEspecial([jose], 3432, 50000, 10000)
conta2.resumo()
print(conta2.saque(100000))
print(conta2.saque(500))
conta2.resumo()

