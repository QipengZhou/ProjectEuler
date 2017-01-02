from itertools import permutations
from Euler import isPrime

def genPandPrimeNum(n_len):
    std_ = '123456789'
    if reduce(lambda x,y: int(x)+int(y), std_[:n_len]) % 3 == 0:
        yield None
    else:
        for i in permutations(std_[:n_len][::-1]):
            if i[-1] not in '24568':
                tmp = int(''.join(i))
                if isPrime(tmp):
                    yield tmp

if __name__ == '__main__':
    res = 2143
    for i in range(9, 3, -1):
        for k in genPandPrimeNum(i):
            if k > res:
                res = k
    print res
