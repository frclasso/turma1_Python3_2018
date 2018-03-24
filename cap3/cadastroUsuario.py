"""Criar um programa cadastroUsuario.py contendo os seguintes dados:
nome, idade, cpf, identidade, nacionalidade, naturalidade, endereço,sexo,
 time de futebol e profissão. O mesmo deve ter tres  saidas, uma pessoal
 ( nome, idade, time de futebol) outra profissional ( nome, identidade,
  cpf e profissão ) e por último, uma completa exibindo todos os dados.
"""

nome = input(("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cpf = input("Digite seu cpf: ")
identidade = input("Digite sua identidade: ")
nacionalidade = input("Digite sua nacionalidade: ")
naturalidade = input("Digite sua naturalidade: ")
endereco= input("Digite seu endereco: ")
sexo= input("Digite seu Sexo: ")
timeDeFutebol= input("Digite seu Time de Futebol favorito: ")
profissao= input("Digite sua Profissao: ")
print("***********************")

print("Seus dados pessoais sao: \nNome: %s   \nIdade %d  "
      "\nTime de futebol %s" % (nome, idade, timeDeFutebol))
print("***********************")
print("Seus dados profissionais sao Nome: %s \nIdentidade: %s "
      "\nCPF: %s \nProfissao: %s" % (nome, identidade, cpf, profissao))
print("***********************")

print("Todos os dados: Nome: %s \nIdade: %d \nCPF: %s "
      "\nIdentidade: %s \nNacionalidade: %s \nNaturalidade: %s "
      "\nEndereco: %s \nSexo: %s \nTime de Futebol: %s "
      "\nProfissao: %s " % (nome, idade, cpf, identidade, nacionalidade,
                          naturalidade, endereco, sexo, timeDeFutebol,
                          profissao))