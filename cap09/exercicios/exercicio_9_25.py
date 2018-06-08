#!/usr/bin/env python3

# -*-coding:utf-8 -*-

"""Altere as funções ​pede_nome ​e ​pede_telefone​ de forma a receberem um
 parâmetro opcional. Caso esse parâmetro seja passado, utilize-o como
 retorno caso a entrada de dados seja vazia."""

agenda = []

# Variável para marcar uma alteração na agenda
alterada = False


# esta funcao foi alterada em relacao ao arquivo 9.23
def pede_nome(padrao=""):
    nome = input("Nome: ")
    if nome == "":
        nome = padrao
    return nome


# esta funcao foi alterada em relacao ao arquivo 9.23
def pede_telefone(padrao=""):
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrao
    return telefone


def mostra_dados(nome, telefone):
    print("Nome: {} Telefone: {}".format(nome, telefone))


def pede_nome_arquivo():
    return input("Nome do arquivo: ")


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def novo():
    global agenda, alterada
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    alterada = True


def confirma(operacao):
    while True:
        opcao = input("Confirma {} (S/N)? ".format(operacao).upper())
        if opcao in "SN":
            return opcao
        else:
            print("Resposta inválida. Escolha S ou N.")


def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p != None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")


def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p != None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone]
            alterada = True
    else:
        print("Nome não encontrado.")


def lista():
    print("\nAgenda\n\n------")
    # Usamos a função enumerate para obter a posição na agenda
    for posicao, e in enumerate(agenda):
        # Imprimimos a posição, sem saltar linha
        print("Posição: {} ".format(posicao, end=""))
        mostra_dados(e[0], e[1])
    print("------\n")


def le_ultima_agenda_gravada():
    ultima = ultima_agenda()
    if ultima != None:
        leia_arquivo(ultima)


def ultima_agenda():
    try:
        arquivo = open("ultima_agenda.dat", "r", encoding="utf-8")
        ultima = arquivo.readline()[:-1]
        arquivo.close()
    except FileNotFoundError:
        return None
    return ultima


def atualiza_ultima(nome):
    arquivo = open("ultima_agenda.dat", "w", encoding="utf-8")
    arquivo.write("{}\n".format(nome))
    arquivo.close()


def leia_arquivo(nome_arquivo):
    global agenda, alterada
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone = l.strip().split("#")
        agenda.append([nome, telefone])
    arquivo.close()
    alterada = False


def le():
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_ultima(nome_arquivo)


def ordena():
    global alterada
    # Você pode ordenar a lista como mostrado no livro
    # com o método de bolhas (bubble sort)
    # Ou combinar o método sort do Python com lambdas para
    # definir a chave da lista
    # agenda.sort(key=lambda e: return e[0])
    fim = len(agenda)
    while fim > 1:
        i=0
        trocou = False
        while i < (fim - 1):
            if agenda[i]>agenda[i + 1]:
                agenda[i], agenda[i+1] = agenda[i+1], agenda[i]
                # temp = agenda[i + 1]
                # agenda[i + 1] = agenda[i]
                # agenda[i] = temp
                trocou = True
            i+=1
        if not trocou:
             break
        for posicao, e in enumerate(agenda):
            # Imprimimos a posição, sem saltar linha
            print("Posição: {} ".format(posicao, end=""))
            mostra_dados(e[0], e[1])
        print("------\n")
    alterada = True


def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w+", encoding="utf-8")
    for e in agenda:
        arquivo.write("{}#{}\n".format(e[0], e[1]))
    arquivo.close()
    atualiza_ultima(nome_arquivo)
    alterada = False


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
                print("Valor inválido, favor digitar entre {} e {}".format(inicio, fim))


def menu():
    print("""
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Grava
   6 - Lê
   7 - Ordena por nome

   0 - Sai
""")
    print("\nNomes na agenda: {} Alterada: {}\n".format(len(agenda), alterada))
    return valida_faixa_inteiro("Escolha uma opção: ",0,7)


le_ultima_agenda_gravada()

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
    elif opcao == 7:
        ordena()
