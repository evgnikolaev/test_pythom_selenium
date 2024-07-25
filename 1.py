'''

Курс питона  - https://stepik.org/course/58852/syllabus



PEP 8 — Python Enhancement Proposal
единый и общепринятый стиль написания программ на языке Python
https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html


1) Ввод
    name = input()
    print('Привет, ', name, '!')


    input('Сколько вам лет?: ')


2) Вывод
    print()
    print('a', '\n', 'b', '\n', 'c', sep='*', end='#')             sep - separator,        end - символ вконце строки



3) Множественное присваивание
    name, surname = 'Timur', 'Guev'
    print('Имя:', name, 'Фамилия:', surname)


    Например для обмена переменными
        name1 = 'Timur'
        name2 = 'Gvido'

        name1, name2 = name2, name1



TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO

Числа и строки

num1 = int(input())
num2 = int(input())

print(num1 + num2)

num = 17
s = str(num)



**	Возведение в степень  вычисляется справа налево x ** y ** z вычисляется как x ** (y ** z).
%	Остаток от деления
//	Целочисленное деление    округление берётся в меньшую сторону  print(-10 // 3)
print(10 // 3)  3   # округление в меньшую сторону
print(-10 // 3)  -4  # округление в меньшую сторону


Операторы // и % имеют такой же приоритет, как и операторы умножения и обычного деления.

Наивысший приоритет имеет оператор возведения в степень **.




TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO

условный оператор

Для разделения команд используются отступы (вместо ";")


if grade >= 90:
    print(1)
elif grade >= 80:
    if grade == 85:
        print(2)
    else:
        print(3)


Цепочки сравнений (от 3 до 6)

if 3 <= age <= 6:
    print('Вы ребёнок')



TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO


Числовые типы данных

    1) int  -  Целочисленный тип данных
            num1 = 25_000_000 (Более удобное написание длинных чисел  num2 = 25000000)
            n = int('12345')

    2) float  -  Числа с плавающей точкой
            e = 2.71828
            num = float(input())

    3) max(), min(), abs()  -  Встроенные функции



Преобразование вещественного в целый:
    int(1.7) = 1      (с округлением в сторону нуля)
    int(-1.7) = -1    (с округлением в сторону нуля)


Функции:
    max(3, 8, -3, 12, 9)
    min(3, 8, -3, 12, 9)
    abs(-7)



TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO


Строковый тип данных

    len('Python rocks!')     - Длина строки
    str(17.77)               - Преобразование чисел в строку
    s1 = 'ab' + 'bc'         - Конкатенация строк
    s = 'Hi' * 4             - Результат HiHiHiHi
    'ab' in 'abc'            - Вхождение подстроки (чувствительно к регистру)


    Тройные кавычки для многострочного текста.

    text = \'''Python is an interpreted, high-level, general-purpose programming language.
    Created by Guido van Rossum and first released in 1991, Python design
    philosophy emphasizes code readability with its notable use of significant whitespace.\'''



TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO


Модуль math

    import math

    num1 = math.sqrt(2)       - вычисление квадратного корня из двух
    num2 = math.ceil(3.8)     - округление числа вверх
    num3 = math.floor(3.8)    - округление числа вниз


Особенности подключения модулей

    from math import *              - позволяет не писать название модуля и символ точки.
    num1 = sqrt(2)

    from math import sqrt, ceil     - подключаем определенные функции модуля
    num1 = sqrt(25)
    num2 = floor(12.8)              - приведет к ошибке, так как функция floor не подключена



TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO




'''

import math

x = float(input())
print(math.floor(x) + math.ceil(x))

if (x > 0):
    print(int(x) + int(x) + 1)
else:
    print(int(x) + int(x) - 1)

d = b * b - 4 * a * c

if d > 0:
    x1 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)

    if x1 < x2:
        print(x1)
        print(x2)
    else:
        print(x2)
        print(x1)

elif d == 0:
    print(-b / (2 * a))
elif d < 0:
    print("Нет корней")
