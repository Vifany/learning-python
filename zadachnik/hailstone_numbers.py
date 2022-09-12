"""Последовательность Коллатца"""

import functools
import time

def hail(tar: int):
    """
     Сдаёт промежуточные числа при вычислении последовательности Коллатца
    и действия выполненные для их получения.
     Аргументы: tar - целое число
     Вывод:
    num - целое число,
    act - булевое значение False при n/2, True при 3n+1
    """
    num = tar
    while num >1:
        if num%2 == 0:
            num = int(num/2)
            act = False
        else:
            num = num*3+1
            act = True
        yield num, act


@functools.cache
def ch_hail (target: int):
    """
    Кешируемое вычисление
    """
    if target%2 == 0:
        target = int(target/2)
        hail_up = False
    else:
        target = target*3+1
        hail_up = True
    return target, hail_up


def depth_search(target: int):
    """
     Формирует последовательность с помощью ch_hail().
    Возвращает глубину и количество итераций.
    """
    depth = 0
    hail_path = []
    while target>1:
        depth += 1
        appendix = ch_hail(target)
        target = appendix[0]
        hail_path.append(appendix)
    return depth, hail_path



def nice_print(target: int):
    """
     Красиво выводит последовательность Коллатца на экран с нумерацией
    и указанием действий в виде '{номер}: действие = результат'
    '"""
    for index, hails in enumerate(hail(target)):
        action_performed = hails[1]
        number_acquired = hails[0]
        previous_number = target
        if action_performed:
            ac = f'{previous_number}*3+1'
        else:
            ac = f'{previous_number}/2'
        print(f'{index}: {ac}  = {number_acquired}')
        previous_number = number_acquired


def deepest(start: int, tar: int):
    """
     Находит наиболее длинную последовательность
    среди чисел в выбранном диапазоне. Выводит на экран число, глубину
    и саму последовательность.
    """
    max_depth = 0
    max_seq = []
    max_i = 0
    max_len = len(range(start,tar))
    for i in range(start, tar):
        depth, seq = depth_search(i)
        if depth > max_depth:
            max_depth = depth
            max_seq = seq
            max_i = i
        print(f' Текущий максимум: {max_depth}    {i}/{max_len}', end='\r' )
    print('')
    print(f'Наибольшая глубина {max_depth} достигнута на числе {max_i}'
            f' c последовательностью:')
    for index, item in enumerate(max_seq):
        if index%10 == 0:
            print('')
        print(item, end ='')

sta = time.perf_counter()
deepest(0, 100000000)
end = (time.perf_counter() - sta)
print(f'Потрачено {end}s')
