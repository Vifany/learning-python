'''
Получает сумму натуральных чисел, кратных 3 и 5, 
от ноля вплоть до введённого числа
'''

def badsum(target):
    ans = 0
    for i in range(target):
        if i%3 == 0 or i%5 == 0: ans +=i
    
    return ans
def main():
    targ = int(input('Введите число: '))
    ans = badsum(targ)
    print(f'Сумма всех чисел от ноля до {targ} кратных 3 или 5 равна: {ans}')
    return

if __name__ == '__main__': main()