"""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу."""

"""
Фуекция, подсчитывающая сумму введенных чисел
"""
def number_input(numstr):
    """
    :param numstr: строка из чисел, введенных через пробел
    :return: сумма чисел из строки
    """
    print(numstr)
    numstr_list = list(numstr)
    print(numstr_list)
    sum = 0
    i = 0
    while i <= len(numstr_list):
        number = numstr_list[i]
        if number.isdigit():
            number = int(number)
            sum = sum + number
            i = i + 2
        else:
            print("Введенный символ не является числом")
            return sum
            exit()
    return sum

"""
Запрос пользователю на ввод строки из чисел с выводом суммы чисел.
После ввода первой строки пользователю предлагается продолжить ввод чисел.
В случае отказа, программа завершается
"""
ssum = 0
y = True
while y:
    numstr = input("Введите строку чисел, разделенных пробелами>>> ")
    ssum = ssum + number_input(numstr)
    print(f"Сумма введенных чисел равна {ssum}")
    choise = input("Хотите продолжить ввод чисел? y/n: ")
    if choise == 'n':
        print("Завершение программы по инициативе пользователя")
        break
    elif choise != 'n' and choise != 'y':
        print("Ошибка выбора")
        break
    else:
        continue