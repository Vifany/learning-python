"""Разлагает число на простые множители"""

import math
import copy
import sympy



def factorize(tar):
    """Факторизует целое число"""
    num = copy.deepcopy(tar)
    prime_lst = [int(x) for x in sympy.primerange(2, int(math.sqrt(num)+1))]
    for prime in reversed(prime_lst):
        while num%prime == 0:
            num = int(num/prime)
            yield prime
            if sympy.isprime(num):
                yield num
                break
        else: continue
        break


def main():
    """Основная функция"""
    tar = int(input('Введите целевое число: '))
    factorizer = factorize(tar)
    print(f'Число {tar} факторизуется как: {next(factorizer)} ', end='')
    for item in factorizer:
        print(f'* {item} ', end ='')


if __name__ == '__main__':
    main()
