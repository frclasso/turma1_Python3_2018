#!/usr/bin/env python3

# -*-coding:utf-8 -*-


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print("CC N°%s Saldo: %10.2f\n" %
              (self.numero, self.saldo))
        for cliente in self.clientes:
            print("Nome: %s\nTelefone: %s\n" % (cliente.nome, cliente.telefone))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.numero)
        for o in self.operacoes:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n    Saldo: %10.2f\n" % self.saldo)


maria = Cliente("Maria", "1243-3321")
joao = Cliente("João", "5554-3322")

conta = Conta([maria, joao], 1234, 5000)
conta.resumo()
