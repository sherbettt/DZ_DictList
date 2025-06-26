#!/usr/bin/env python3.12

def fibonacci_dict(n):
    # инициализация результата словаря
    result = {}
    
    # Создание ряда Фибоначчи от нуля до макисмального
    fib = [0, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    
    # Создание словаря для каждого индекса от 0 до n
    for i in range(n + 1):
        # Добавить все числа Фибоначчи, которые меньше текущего ключа.
        result[i] = [x for x in fib if x < i]
        
    return result

print(fibonacci_dict(5))
