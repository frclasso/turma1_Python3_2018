
def media(*valores):
    total=0.0
    for x in valores: total+= x
    return total/len(valores)


def main():
    print(media(1, 2, 3, 4, 5))


if __name__ == '__main__':main()
