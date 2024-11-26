# Генераторные сборки
import sys

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

print('\nРезультат работы генераторной сборки:')
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(f'тип объекта: {type(first_result)}') # вывод типа объекта - generator
print(list(first_result)) # вывод результата работы генераторной сборки
print(f'тип объекта: {type(second_result)}') # вывод типа объекта - generator
print(list(second_result)) # вывод результата работы генераторной сборки


print('\nРезультат переделки в списочную сборку:')
first_result = [abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s)]
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]

print(f'тип объекта: {type(first_result)}') # вывод типа объекта
print(first_result) # вывод результата работы сборки
print(f'тип объекта: {type(second_result)}') # вывод типа объекта
print(second_result) # вывод результата работы сборки
