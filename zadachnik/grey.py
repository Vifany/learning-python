"""Выводит код Грея для всех пятибитных двочиных чисел"""


def grey(num: int):
    """Генерирует код Грея для заданного положительного числа"""
    if num<0: raise ValueError('Number must be positive')
    s_num = num >> 1
    grey_num = num ^ s_num
    return grey_num

def main():
    """Основная функция"""
    for num in range(31):
        print(f'Число {num} имеет двоичное представление '
            f'{bin(num)} и код Грея {bin(grey(num))}')

if __name__ == '__main__':
    main()
