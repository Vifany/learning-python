'''
Выводит наименьшее общее кратное
'''

def multiple(num1, num2):
    tar = (num1*num2)+1
    if num1 < num2: lowlim = num1
    else: lowlim = num2
    for i in range(lowlim, tar):
        if i % num1 == 0 and i % num2 == 0: return i


def main():
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    minmul = multiple(num1, num2)
    print(f'Наименьшее общее кратное чисел {num1} и {num2} равно: {minmul}')
    return


if __name__=='__main__': main()