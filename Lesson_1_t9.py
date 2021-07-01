"Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."
a = int(input('Введите значение первого числа: '))
b = int(input('Введите значение второго числа: '))
c = int(input('Введите значение третьего числа: '))
medium = 0

if  a < b < c or c < b < a:
    medium = medium + b
elif b < a < c or c < a < b:
   medium = medium + a
else:
   medium = medium + c

print(f'Среднее значение: {medium}')