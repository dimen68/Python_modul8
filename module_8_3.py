# Задача "Некорректность"
class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_num):
        if not isinstance(vin_num, int):
            raise IncorrectVinNumber(f'Некорректный тип vin номер: {vin_num}')
        elif vin_num not in range(1000000, 9999999):
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера: {vin_num}')
        else:
            return True

    def __is_valid_numbers(self, car_num):
        if not isinstance(car_num, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров: {car_num}')
        elif len(car_num) != 6:
            raise IncorrectCarNumbers(f'Неверная длина номера: {car_num}')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message='Что-то не так с Vin-номером'):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message='Что-то не так с номерами'):
        self.message = message


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        fifth = Car('Model5', 'потом_поставим', 'f456dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{fifth.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

    try:
        fourth = Car('Model4', 2020202, 123456)
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{fourth.model} успешно создан')
