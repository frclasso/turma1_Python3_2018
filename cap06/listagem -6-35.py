'''Controle de utilizacao de uma sala de cinema'''

lugares_vagos = [10,2,1,3,0]
while True:
    sala = int(input('Sala (0 para sair): '))
    if sala  == 0:
        break
    if sala > len(lugares_vagos) or sala < 1:
        print('Sala invalida')
    elif lugares_vagos[sala - 1] == 0:
        print('Sala lotada!')
    else:
        # lugares = int(input('Quantos lugares voce deseja? (%d vagos):'
        #                     % lugares_vagos[sala -1]))
        lugares = int(input('Quantos lugares voce deseja? '
                            '{} vagos:'.format(lugares_vagos[sala-1])))

        if lugares > lugares_vagos[sala-1]:
            print('Esse numero de lugares nao esta disponivel')
        elif lugares < 0:
            print('Numero invalido')
        else:
            lugares_vagos[sala-1] -= lugares
            print(f'{lugares} lugares vendidos')
print('Utilizacao das salas')
for x,l in enumerate(lugares_vagos):
    print(f'Sala {x + 1} - {l} lugar(es) vazio(s)')
