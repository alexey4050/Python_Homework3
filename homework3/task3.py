# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print("Найти разницу между макс и мин значениями дробной части вещечтвенных чисел.")
print("-" * 80)

from random import uniform

number = int(input("Введите длину строки: "))

list = []
for i in range(number):
    f = uniform(0, 9)
    list.append(round(f, 2))
    
min = list[0]
max =0
for i in range(len(list)):
    
    if(max < list[i]):
        max = list[i]
    if(min > list[i]):
        min = list[i]
dif = (max - int(max)) - (min - int(min))

print(f"Список -> {list}\n")
print(f"Разница между {max} и {min} дробной части = {round(dif, 2)}\n")