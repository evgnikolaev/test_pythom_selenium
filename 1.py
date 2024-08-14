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
       x, y = y, x

                Тоже самое, что:
                        temp = x
                        x = y
                        y = temp



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

Цикл for

        range(n)            - от 0 до n-1
        range(n, m):        - от n  до  m - 1.
        range(n, m, k)      - от n  до  m - 1 , с шагом k.

        range(7, 3)	        пустая последовательность
        range(3, 10, -2)    пустая последовательность

     for i in range(10):
            print(i, '-- Привет')

        _ когда переменная цикла не используется в теле цикла.
        for _ in range(5):
            print('Python - awesome!')


    break     - прерывает цикл
    continue  - прерывает итерацию



Цикл while

       str = input()
       while str != "стоп" and str != "хватит"
            .....
            str = input()



        Обработка цифр числа

        n = int(input())
        while n != 0:                  пока в числе есть цифры
            last_digit = n % 10        получить последнюю цифру
            ........                   код обработки последней цифры
            n = n // 10                удалить последнюю цифру из числа




Блок else в циклах

    Если же слово else присутствует, то блок кода2 будет выполняться только в том случае,
    если цикл завершается штатным образом.
    Под штатным завершением цикла подразумевается его завершение без использования оператора прерывания break.

    Если цикл преждевременно завершается с помощью оператора прерывания break, то блок кода в инструкции else не будет выполнен.


        while условие:
            блок кода1
        else:
            блок кода2

        # или

        for i in range(10):
            блок кода1
        else:
            блок кода2



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


    Индексация строк

        Положительные индексы	 0	 1	 2	 3	 4	 5
        Строка	                 P	 y	 t	 h	 o	 n
        Отрицательные индексы	-6	-5	-4	-3	-2	-1

        отрицательные индексы строки начинаются с -1

        s[0]    P
        s[-6]	P


    Итерирование строк
        s = 'abcdef'
        for i in range(len(s)):
        print(s[i])


        s = 'abcdef'
        for c in s:         с - переменная, назвали прсосто - первая буква слова char (символ).
            print(c)

        Этот цикл пройдет по строке s, придавая переменной цикла c значение каждого символа (!) в отличие от предыдущего цикла,
        в котором переменная цикла «бегала» по индексам строки.



Срезы строк

    Положительные индексы	    0	1	2	3	4	5	6	7	8	9
    Строка	                    a	b	c	d	e	f	g	h	i	j
    Отрицательные индексы	    -10	-9	-8	-7	-6	-5	-4	-3	-2	-1

    отрицательные индексы строки начинаются с -1

s[x:y:шаг]
    x - включительно,
    y - невключительно
    Если в качестве шага среза указать отрицательное число, то символы будут идти в обратном порядке.

        s[2:5]      от 2 до 5 (cde)
        s[2:]       от 2 до конца (cdefghij)
        s[:7]       от начала до 7 (abcdefg)
        s[:]        возвращает исходную строку.
        s[-9:-4]    (bcdef)
        s[:-1]      от начала до -1 (abcdefghi) , Удалить из строки последний символ

        s[1:7:2]   взяты индексы 1,3,5 (bdf)
        s[::-1]    Если в качестве шага среза указать отрицательное число, то символы будут идти в обратном порядке. (jihgfedcba)


Изменение символа строки по индексу

    В Python строки являются неизменяемыми, то есть мы не можем менять их содержимое с помощью индексатора.
    s[4] = 'X'                  - не сработает
    s = s[:4] + 'X' + s[5:]     - сработает, мы должны создать новую строку


'''

n = int(input())
txt = str()
while n > 0:
    txt = str(n % 2) + txt
    n = n // 2
print(txt)



# s = input()
# count_1 = 0
# count_2 = 0
# for i in range(len(s)):
#     if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         count_1 = count_1 + 1
#     if s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         count_2 = count_2 + 1
#
# print("Количество гласных букв равно", count_1)
# print("Количество согласных букв равно", count_2)
