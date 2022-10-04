# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def NegaFib(n):
    list = []
    for i in range(n * 2 + 1):
        list.append(0)
    list[n - 1] = list[n + 1] = 1
    for i in range(n - 1):
        list[n + 2 + i] = list[n + 1 + i] + list[n + i]
        list[n - 2 - i] = list[n - i] - list[n - 1 - i]
    return list

n = int(input("Введите количество элементов: "))
nega_fib = NegaFib(n)
print(nega_fib)