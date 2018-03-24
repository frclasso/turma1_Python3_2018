'''Normalmente, pagamos o Imposto de renda por faixa de salário.
Imagine que para salarios menores que R$1.000,00 nao teriamos imposto a
pagar, ou seja, alíquota 0%. Para salários entre R$1.000,00 e R$3.000,00
pagamos 20%. Acima desses valores ,a alíquota seria de 35%.
Esse problema se pareceria muito com o anterior, salvo se o
imposto não fosse cobrado diferentemente para cada faixa,
ou seja, quem ganha R$4.000,00 tem os primeiros R$1.000,00
isentos de impostos; com o montante entre R$1.000,00 e R$3.000,00
pagando 20%, e restante pagando os 35%.
'''

salario = float(input("Digite salario: "))
base = salario
imposto = 0

if base > 3000:
    imposto = imposto + ((base -3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print("Salrio: R$%.2f Imposto a pagar R$%.2f " % (salario, imposto))