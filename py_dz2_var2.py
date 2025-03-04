n = int(input("Введи индекс ряда Фибоначчи: "))
if n==0:
    fib=[0]
elif n==1:
    fib=[0,1]
else:
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
print(fib)
