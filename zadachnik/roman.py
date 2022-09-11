"""Преобразует целое положительное число в строку с римским числом"""


DIC_ROM ={
    1:'I',
    4:'IV',
    5:'V',
    9:'IX',
    10:'X',
    40:'XL',
    50:'L',
    90:'XC',
    100:'C',
    400:'CD',
    500:'D',
    900:'CM',
    1000:'M'
}


def fact_rom(num: int):
    """Преобразует целое положительное число в строку с римским числом"""
    if num >3999 :
        raise ValueError('Number must be less than 3999')
    if num <=0 :
        raise ValueError('Number must be more than 0')
    facted_list = []
    for roma in reversed(DIC_ROM):
        while num>=roma:
            num = num - roma
            if roma not in facted_list[-1:-3]:
                facted_list.append(DIC_ROM[roma])
    return ''.join(facted_list)


def main():
    """Штат Мейн"""
    i = input('Введите число: ')
    print(f'{fact_rom(i)}')

if __name__ == '__main__':
    main()