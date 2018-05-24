def fibo(n):
    'Print a Fibonnaci series up to n.'
    a,b = 0,1
    while a < n:
        print(a, end=' ', flush=True)
        a,b = b, a + b
    print()


fibo(60)
print(fibo.__doc__)