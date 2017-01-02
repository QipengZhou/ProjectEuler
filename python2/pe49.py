from collections import defaultdict
from itertools import combinations
from Euler import xsieveErato

def seqPrimes(nth, nd=3):
    res = []
    tmp = defaultdict(list)
    for i in xsieveErato(pow(10, nth+1)):
        i_str = str(i)
        if len(i_str) == nth:
            tmp[''.join(sorted(i_str))].append(i)
    for k in tmp:
        for v in combinations(tmp[k], nd):
            a = sorted(v)
            flag = a[1] - a[0]
            for j in range(2, nd):
                if (a[j] - a[j-1]) != flag:
                    break
            else:
                res.append(a)
    return res

if __name__ == '__main__':
    for i in seqPrimes(4):
        tmp = reduce(lambda x,y: str(x)+str(y), i, '')
        if tmp != '148748178147':
            print tmp
