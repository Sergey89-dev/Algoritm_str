"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
"""
import math
import timeit


def not_erat(i):
    '''Алгоритм без использования «Решета Эратосфена»
    '''

    list_ = [2]
    number = 3
    while len(list_) < i:
        rej = True
        for a in list_.copy():
            if number % a == 0:
                rej = False
                break
        if rej:
            list_.append(number)
        number += 1
    return list_[-1]
NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000

def erat(n):
    "С использованием алгоритма"
    user = 1
    start = 3
    end = 4 * n

    proc = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while user < n:

        for i in range(len(proc)):

            if proc[i] != 0:
                user += 1

                if user == n:
                    return proc[i]

                j = i + proc[i]

                while j < len(proc):
                    proc[j] = 0
                    j += proc[i]

        prime.extend([i for i in proc if i != 0])

        start, end = end, end + 2 * n
        proc = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(proc)):

            for num in prime:

                if proc[i] % num == 0:
                    proc[i] = 0
                    break

time1 = timeit.timeit(f'not_erat({TEST_VALUE})',
                      setup='from __main__ import not_erat',
                      number=NUMBER_EXECUTIONS)

time2 = timeit.timeit(f'erat({TEST_VALUE})',
                      setup='from __main__ import erat',
                      number=NUMBER_EXECUTIONS)

print(f'Программа без использования алгоритма «Решето Эратосфена» быстрее \
программы с использованием алгоритма «Решето Эратосфена» в \
{round(time2 / time1, 2)} раз'
      )