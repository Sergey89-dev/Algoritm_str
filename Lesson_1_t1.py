"Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."
from functools import reduce
import operator
a =list(map(int, input('Введите трехзначное число через пробел: ').split()))
if len(a) == 3:
    print('Сумма цифр в числе = ', sum(a))
    end = reduce(operator.mul, a, 1)
    print(f'Произведение чисел в числе: {end}')

else:
    print('Пожалуйста введите 3 значное число')