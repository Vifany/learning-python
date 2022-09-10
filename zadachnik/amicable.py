u"""Выводит дружественные числа вплоть до заданного"""

from abundant import divisors

def list_divsum(tar):
    u"""Сдаёт сумму делителей tar"""
    for i in range(tar):
        yield int(sum(divisors(i)))


def search_amicable(tar):
    u"""Сдаёт пары дружественных чисел вплоть до tar"""
    divlist = list(list_divsum(tar))
    for i, item in enumerate(divlist):
        if item <= len(divlist):
            if divlist[item] == i and i != item:
                yield i, item


def main():
    u"""Основная функция"""
    clearing_set = set()
    for i, item in search_amicable(100000):
        if i not in clearing_set:
            print(f'{i} amicable to {item}')
            clearing_set.add(item)


if __name__ == '__main__':
    main()
