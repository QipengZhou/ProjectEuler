from itertools import permutations
from Euler import xsieveErato, isPrime

def isL2RPrime(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if not isPrime(int(n_str[i:])):
            return False
    return True

def isR2LPrime(n):
    n_str = str(n)
    n_len = len(n_str)
    for i in range(len(n_str)):
        if not isPrime(int(n_str[:(n_len-i)])):
            return False
    return True

def isLegal(n):
    n_str = str(n)
    for i in '024568':
        if i in n_str:
            return False
    return (n_str[-1] in '37')

if __name__ == '__main__':
    ans = []
    for i in permutations([2, 3, 5, 7], 2):
        tmp = i[0] * 10 + i[1]
        if isL2RPrime(tmp) and isR2LPrime(tmp):
            ans.append(tmp)
    tot = [3, 7]
    for i in range(100):
        aa = []
        for k in '37':
            aa.extend([int(k+str(j)) for j in tot if isPrime(int(k+str(j)))])
        for k in aa:
            if isR2LPrime(k):
                ans.append(k)
        for k in '19':
            aa.extend([int(k+str(j)) for j in tot if isPrime(int(k+str(j)))])
        if not aa:
            break
        tot = aa[:]

    print sum(set(ans))
