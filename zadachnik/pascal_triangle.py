"""
Генерирует треугольник Паскаля с заданным числом строк.
"""
import numpy

def tristring(prev_str):
    """Генерирует следующую строку треугольника по предыдущей"""
    res = []
    prev = 0
    for index, value in enumerate(prev_str):
        cur = value+prev
        prev = value
        res.append(cur)
        if index == len(prev_str)-1:
            res.append(value)
    return res

def triangle (depth: int = 15, base: int = 1):
    """Построчно генерирует треугольник"""
    triang = [base, [base, base]]
    for i in range(1, depth):
        triang.append(tristring(triang[i]))
    return triang

def cuteprint(triang: list):
    """Некрасивый код который красиво выводит треугольник на экран"""
    maxlen = len(triang[-1])
    separator =len(str(max(triang[-1])))
    spacer = ' '*(separator)
    align = spacer * (maxlen - 1 )
    print(f'{align}{triang[0]: ^{separator}}')
    for index, item in enumerate(triang[1:-1]):
        align = spacer * (maxlen - 3 - index)
        print(align, end ='')
        for it in item:
            print(f'{spacer}{it: ^{separator}}', end = '')
        print('')

def main():
    """Штат Мэйн"""
    triang = triangle()
    cuteprint(triang)

if __name__ == '__main__':
    main()
