'''
Определяет наибольший общий делитель введёных чисел
'''

def dividor(higher, lower):
    tar = int(lower/2)
    if higher % lower ==0: return lower
    for i in reversed(range(tar)):
        if higher % i == 0 and lower % i == 0: return i
    return


def divfun(num1, num2):
    if num1>num2: ans = dividor(num1, num2)
    elif num1<num2: ans = dividor(num2, num1)
    else: ans =  num1
    print(f'Наибольший общий делитель чисел {num1} и {num2} равен: {ans}')
    return

def main():
    num1 = 0
    num2 = 0
    while True:
        num1 = int(input('Введите первое число:'))
        num2 = int(input('Введите второе число: '))
        if num1>0 and num2>0: break
        else: print('Оба числа должны быть положительными, введите числа заново.')
    divfun(num1, num2)
    return

if __name__ == '__main__': main()