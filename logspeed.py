"""
Сравнивает скорость поиска ближайшей к числу степени двойки через
итерации и логарифм
 """

import math
import time
import functools
from numpy import mean

def timer(func):
    """Выводит производительность"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter_ns()
        value = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        run_time = end_time - start_time
        return value, run_time
    return wrapper_timer

@timer
def iterative(tar):
    """Итеративно"""
    x = 0
    while 2**x < tar:
        x+=1
    return x

@timer
def logarithmic(tar):
    """Логарифмически"""
    x=int(math.log(tar,2))
    return x




def main():
    """Штат Мэйн()"""
    arlog = []
    ariter = []
    for i in range(2,1000000):
        val, time = logarithmic(i)
        arlog.append(time)
        val, time = iterative(i)
        ariter.append(time)

    mlolg = mean(arlog)
    miter = mean(ariter)
    print(f'Среднее время логарифмически: {mlolg:.2f}нс, среднее время итеративно {miter:.2f}нс')

if __name__ == '__main__':
    main()