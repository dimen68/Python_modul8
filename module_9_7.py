# задание по теме "Декораторы"

def is_prime(func):
    def wrapper(*args, **kwargs):
        res_ = func(*args, **kwargs)
        n = 0
        for i in range(2, res_ // 2 + 1):  # проверка на простоту
            if res_ % i == 0:
                n = n + 1
        if n <= 0:
            print("Простое: ", end="")
        else:
            print("Составное: ", end="")
        return res_  # возвращаем результат проверки (простое или составное)

    return wrapper  # возвращаем функцию для расчетов


@is_prime
def sum_three(a, b, c):  # функция суммирования трех чисел
    res_sum1 = a + b + c
    return res_sum1


@is_prime
def sum_any(*args):  # функция суммирования любого количества чисел
    res_sum2 = 0
    for k in args:
        res_sum2 += k
    return res_sum2


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
    result = sum_three(1, 2, 3)
    print(result)
    result = sum_three(4, 5, 6)
    print(result)
    print()

    result = sum_any(4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
    print(result)
    result = sum_any(1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14)
    print(result)
