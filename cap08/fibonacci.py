def fibo(n):
    a,b =  0,1
    while b < 10000:
        print(b, flush=True)
        a,b = b, a+ b
    print()
fibo(60)