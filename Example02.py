"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
"""
Программа принимает данные от пользователя (имя, фамилия, год рождения, город проживания, email, телефон)
и выводит их в одну строку
"""
# Получение данных от пользователя
name = input("Введите имя>>> ")
surname = input("Введите фамилию>>> ")
birth_year = input("Введите год рождения>>> ")
city = input("Введите город проживания>>> ")
email = input("Введите email>>> ")
phone = input("Введите телефон>>> ")

# Определение функции, записыващей данные о пользователе в одну строку
def user_data(name, surname, birth_year, city, email, phone)
    """
    :param name: имя пользователя
    :param surname: фамилия пользователя
    :param birth_year: год рождения пользователя
    :param city: город проживания пользователя
    :param email: адрес электронной почты пользователя
    :param phone: номер телефона пользователя
    """
    user_data = []
    user_data.append(name)
    user_data.append(surname)
    user_data.append(birth_year)
    user_data.append(city)
    user_data.append(email)
    user_data.append(phone)
    for data in range(len(user_data)):
        print(user_data[data], end = " ")

# Вызов функции с параметрами - данными, введенными пользователем
user_data(name, surname, birth_year, city, email, phone)
