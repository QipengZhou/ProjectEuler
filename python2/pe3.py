import math
from collections import defaultdict

def isSquare(N):
    return (N - int(math.sqrt(N)) ** 2) < 1e-12

def fermatfactor(N):
    a = int(math.ceil(math.sqrt(N)))
    b = a * a - N
    while not isSquare(b):
        a += 1
        b = a * a - N
    return (a - int(math.sqrt(b)), a + int(math.sqrt(b)))

def normOdd(N):
    count = 0
    while N % 2 == 0:
        N = N / 2
        count += 1
    return (N, count)

def wrapDict(key, dict_, val):
    if key in dict_:
        dict_[key] += val
    else:
        dict_[key] = val

def factors(N):
    res = defaultdict(int)
    n1, n2 = normOdd(N)
    if n1 == 1:
        return {2:n2}
    n = {n1:1}
    while n:
        n1 = n.keys()[0]
        fact1, fact2 = fermatfactor(n1)
        nc = n.pop(n1)
        if fact1 == 1:
            res[fact2] += nc
            continue
        if fact1 in res:
            res[fact1] += nc
        else:
            wrapDict(fact1, n, nc)
            wrapDict(fact2, n, nc)
    return res
