'''
Выводит избыточные числа и величину их избыточности вплоть до указанного
'''
import math

def divisors(x):
    large_divisors = []
    for d in range(2, int(math.sqrt(x)+1)):
        if x%d == 0:
            yield d
            if d*d !=x: large_divisors.append(x/d)
    for div in large_divisors: yield div
    
def abundance(n):
    ab = sum(divisors(n)) - n
    if ab > 0: return ab
    else: return None

def abundant_list(tar):
    for n in range(tar):
        ab = abundance(n)
        if ab != None: yield n, ab

def main():
    tar = int(input('Введите число: '))
    for n, ab in abundant_list(tar):
        print(f'Сумма делителей числа {n} превышает само число на {ab}')
    return

if __name__ == '__main__': main()