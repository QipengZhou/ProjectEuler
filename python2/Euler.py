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
