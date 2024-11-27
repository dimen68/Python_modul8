# Задача "Функциональное разнообразие"

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

result_1 = list(map(lambda x, y: x == y, first, second))
print(result_1)

# Замыкание:
import os


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        if not os.path.isfile(file_name):
            with open(file_name, 'w', encoding='utf-8') as file:
                for item in data_set:
                    file.write(str(item) + '\n')
        else:
            with open(file_name, 'a', encoding='utf-8') as file:
                for item in data_set:
                    file.write(str(item) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
from random import choice


class MysticBall:
    def __init__(self, *words):
        word_list = []
        for w in words:
            word_list.append(w)
        self.word_list = word_list

    def __call__(self):
        return choice(self.word_list)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
