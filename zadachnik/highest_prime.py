'''
Выводит наибольше простое число меньше заданного
'''

import sympy

def main():
    tar = int(input('Введите целевое число: '))
    prime_arr = sympy.primerange(tar/2, tar)
    ans = max(prime_arr)
    print(f'Самым большим простым числом до {tar} является: {ans}')
    return

if __name__ == '__main__': main()