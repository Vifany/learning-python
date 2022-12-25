import itertools
import string
def decompose_int(val):
    '''Decomposes int into tuple with count of used digits'''
    return tuple([str(val).count(i) for i in string.digits])

def searchlist(amount: int, power: int):
    '''
    Searches lowest base of exponent with set amount
    of permutations which have integer root of same power
    '''
    key = itertools.count()
    retlist = []
    while True:
        retlist.append(decompose_int(pow(next(key),power)))
        if retlist.count(retlist[-1]) == amount:
            return pow(retlist.index(retlist[-1], 0), power)

if __name__ == '__main__':
    print(searchlist(5, 3))
