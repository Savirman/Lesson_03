"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
"""
Программа выполняет деление двух целых чисел, вводимых пользователем
"""

"""
Функция ввода делимого с проверкой пользовательского ввода (является ли введенное числом)
"""
def num_input():
    """
    :return: делимое - число, введенное пользователем, после проверки
    :rtype int
    """
    while True:
        number = input("Введите делимое>>>")
        if number.isdigit():
            number = int(number)
            return number
        else:
            print('Ошибка данных, введено не число')

"""
Функция ввода делителя с проверкой пользовательского ввода (является ли введенное числом, не равным нулю)
"""
def den_input():
    """
    :return: делитель - число, введенное пользователем после проверки
    :rtype int
    """
    while True:
        number = input("Введите делитель>>>")
        if number.isdigit():
            number = int(number)
            if number != 0:
                return number
            else:
                print("Ошибка! Делить на ноль нельзя! Введите число, не равное нулю.")
        else:
            print('Ошибка данных, введено не число')

"""
Функция выполнения деления чисел, введенных пользователем
"""
def div_two_num(numerator, denumerator):
    """
    :param numerator: делимое
    :param denumerator: делитель
    :return: частное от деления
    """
    quot_of_div = numerator / denumerator
    return quot_of_div

dividend = num_input()
print(dividend)
divider = den_input()
print(divider)
result = div_two_num(dividend, divider)
print(f"Результат деления: {result}")
