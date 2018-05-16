
def par(x):
    return x % 2 == 0


def par_ou_impar(x):
    if par(x):
        return 'par'
    else: return 'impar'


def main():
    print(par_ou_impar(4))
    print(par_ou_impar(3))


if __name__=="__main__":main()