def calcula_tempo(velocidade, distancia):
    tempo = distancia/velocidade
    velocidade = 0
    return tempo

def calcula_distancia(velocidade, tempo):
    distancia = velocidade * tempo
    return distancia


v = 10
t = calcula_tempo(v, 5)
print(v)
print(t)
d = calcula_distancia(v, t)
print(d)