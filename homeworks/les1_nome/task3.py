'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

num = int(input('Введите число n от 1 до 9: '))
if 0 < num < 10:
    print(f"Сумма чисел {num} + {num * 11} + {num * 111} составит {num * 123}")
else:
    print('Вы ввели неверное число!')