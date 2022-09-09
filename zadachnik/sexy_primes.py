'''
Выводит все простые числа отличающиеся на шесть меньше заданного
'''

import sympy
import copy


def sexy(tar):
    primes = list(sympy.primerange(2, tar))
    ans = []
    for i, p in enumerate(primes):
        if p-6 == primes[i-1]:
            toap = [p, primes[i-1]]
            ans.append(copy.deepcopy(toap))
    return ans

def main():
    targ = int(input('Введите целевое число: '))
    sexy_arr = sexy(targ)
    for item in sexy_arr:
        print(f'{item[1]} и {item[0]}')
    return

if __name__=='__main__': main()