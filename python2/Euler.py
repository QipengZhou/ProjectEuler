import math

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
