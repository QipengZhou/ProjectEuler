from Euler import properDivisors
from itertools import combinations, ifilter

def isAbundant(n):
    return n < sum(properDivisors(n))

if __name__ == '__main__':
    tmp = [i for i in range(12, 28124) if isAbundant(i)]
    res = []
    tot = (1+28123)*28123/2
    for i in range(len(tmp)):
        if tmp[i] > 28123/2+1:
            break
    a = tmp[:i]
    b = tmp[i:]
    for i in combinations(a, 2):
        tt = sum(i)
        res.append(tt)
    res = ifilter(lambda x: x < 28124, res)
    res_set = set(res)
    res1 = []
    for i in a:
        for j in b:
            if i + j < 28124:
                res1.append(i+j)
    t = [2*i for i in tmp if 2*i < 28124]
    print tot - sum(res_set.union(set(res1)).union(set(t)))
