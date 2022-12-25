import itertools
import string
def decompose_int(val):
    '''Decomposes int into list with count of used digits'''
    return [str(val).count(i) for i in string.digits]

def searchlist(amount, power):
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

print(searchlist(5, 3))