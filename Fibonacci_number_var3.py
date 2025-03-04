from math import sqrt

fib_dict = {0: 0, 1: 1}

def fibonacci_dp(n):
    if n not in fib_dict:
        fib_dict[n] = fibonacci_dp(n-1) + fibonacci_dp(n-2)
    return fib_dict[n]

print('значение:' , fibonacci_dp(10))
