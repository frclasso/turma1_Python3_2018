def main():
    x = ('Florianopolis', 'Python', 'Brasil', 'Go', 'Django')
    palavras(*x)


def palavras(*args):
    if len(args): #caso tenha pelo menos um argumento
        for s in args:print(s)
    else:print('Sem parametros pre-definidos') #caso nao receba parametros


if __name__=="__main__":main()