import math
from collections import defaultdict

def sieveErato(n):
    """Find all primes below n."""
    if n < 2: return []
    flag = [1] * n
    flag[0] = 0
    flag[1] = 0
    for i in range(2, int(math.sqrt(n))+1):
        if flag[i]:
            for j in range(i*i, n, i):
                flag[j] = 0
    ans = []
    for i in range(len(flag)):
        if flag[i]:
            ans.append(i)
    return ans

def xsieveErato(n):
    """Find all primes below n."""
    if n < 2: yield None
    flag = [1] * n
    flag[0] = 0
    flag[1] = 0
    for i in range(2, int(math.sqrt(n))+1):
        if flag[i]:
            for j in range(i*i, n, i):
                flag[j] = 0
    for i in range(len(flag)):
        if flag[i]:
            yield i

def triangleNum(n):
    return n*(n+1)/2

def factorNum(n):
    res = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            res += 2
    if int(math.sqrt(n)) ** 2 == n:
        res -= 1
    return res

def isLeap(year):
    if year % 400 == 0:
        return True
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    return False

def properDivisors(n):
    res = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            res.append(i)
            a = n / i
            if a not in res:
                res.append(a)
    return [1] + res if res else res

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

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
    if n2:
        res[2] = n2
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

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

def isPalindromic(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def genPalindromics(a, b):
    for i in range(a, b):
        if isPalindromic(i):
            yield i

def isPandigital(n, all=False):
    std_ = '123456789'
    n_str = str(n)
    num = 9 if all else len(n_str)
    return ''.join(sorted(n_str)) == std_[:num]

def triangleNum(n):
    if n <= 0:
        return 0
    delta_ = 1 + 8*n
    delta_sqrt = squareNum(delta_)
    return (delta_sqrt-1)//2 if (delta_sqrt-1)%2 == 0 else 0

def pentagonalNum(n):
    if n <= 0:
        return 0
    delta = 1+24*n
    delta_sqrt = squareNum(delta)
    return (delta_sqrt+1)//6 if (delta_sqrt+1)%6 == 0 else 0

def squareNum(n):
    n_s = int(math.sqrt(n))
    if abs(n_s*n_s - n) < 1e-30:
        return n_s
    return 0

def primeFactorsNum(n):
    res = 0
    a = int(math.sqrt(n))
    for i in range(2, a + 1):
        if n % i == 0:
            res += 1
            while n % i == 0:
                n /= i
    if n != 1:
        res += 1
    return res
