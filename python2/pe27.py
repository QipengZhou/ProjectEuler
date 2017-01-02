from Euler import sieveErato
from Euler import isPrime
import math

def quadPrimes(a, b):
    for i in range(1, b):
        num = i * i + a * i + b
        if num < 0:
            break
        if isPrime(num):
            continue
        else:
            break
    return i

if __name__ == '__main__':
    bn = sieveErato(1001)
    n = 1
    for b in bn:
        tt = int(math.sqrt(b)) + 1
        for a in range(-2*tt-1, 2*tt):
            qp = quadPrimes(a, b)
            if qp > n:
                n = qp
                na = a
                nb = b
    print n, na, nb, na * nb
