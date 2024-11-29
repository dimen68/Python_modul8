# Задача "Range - это просто"

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = int(start)  # целое число, с которого начинается итерация
        self.stop = int(stop)  # целое число, на котором заканчивается итерация
        if step == 0:
            raise StepValueError
        else:
            self.step = int(step)  # шаг, с которым совершается итерация
        self.pointer = self.start  # указывает на текущее число в итерации (изначально start)

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration
        elif self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        result_ = self.pointer
        self.pointer += self.step
        return result_


if __name__ == '__main__':
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('Шаг указан неверно')

    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)

    for i in iter2:
        print(i, end=' ')
    print()
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()