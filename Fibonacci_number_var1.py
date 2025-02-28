# Число Фибоначчи
def fib():
    f1, f2 = 0, 1
    while True:
        yield f1
        f1, f2 = f2, f2 + f1

for i, f in zip(range(11+1), fib()):
    print("{i:3}: {f:3}".format(i=i, f=f))
