'''
<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>

'''

n = int(input())
count1, count2, count3, count4, summ1 = 0, 0, 0, 0, 0
proizv1 = 1

last_num = n % 10

while n != 0:
    last_digit = n % 10

    if last_digit == 3:
        count1 = count1 + 1

    if last_digit == last_num:
        count2 = count2 + 1

    if last_digit % 2 == 0:
        count3 = count3 + 1

    if last_digit > 5:
        summ1 = summ1 + last_digit

    if last_digit > 7:
        proizv1 = proizv1 * last_digit

    if last_digit == 0 or last_digit == 5:
        count4 = count4 + 1

    n = n // 10

print(count1)
print(count2)
print(count3)
print(summ1)
print(proizv1)
print(count4)
