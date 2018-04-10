'''Exercício 5.9 Escreva um programa que leia dois números. Imprima a
divisão inteira do primeiro pelo segundo, assim como o resto da divisão.
Utilize apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender o quociente da divisão de dois números
como a quantidade de vezes que podemos retirar o divisor do dividendo.
Logo, 20 / 4 = 5, uma vez que podemos subtrair “4” cinco vezes de 20.
'''

dividendo = int(input('Dividendo: '))
divisor = int(input('Divisor: '))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1

resto = x
print('%d / %d = %d(quociente) %d(resto)' % (dividendo, divisor, quociente, resto))