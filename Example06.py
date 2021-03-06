"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

"""
Программа получает слово (и строку из слов) из малеьних латинских букв и преобразует первую букву слова в заглавную.
"""

"""
Функция преобразования перовй буквы слова в заглавную
"""
def int_func(word):
    word = word.title()
    print(word)

"""
Функция преобразования первой буквы в заглавную с каждом слове в строке
"""
def str_func(words):
    int_func(words)

# Ввод пользователем слова из маленьких латинских букв
user_word = input("Введите слово из маленьких латинских букв>>> ")
int_func(user_word)

# Ввод пользователем строки из слов, написанных маленькими латинскими буквами
user_str = input("Введите строку из слов, разделенных пробелами>>> ")
str_func(user_str)