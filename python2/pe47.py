from itertools import combinations
from Euler import factors, primeFactorsNum

def isFactorsDistinct(a, b):
    a_b = set(a).intersection(set(b))
    for i in a_b:
        if a[i] == b[i]:
            return False
    return True

def isAllFactorsDistinct(sq):
    sq_len = len(sq)
    return all([isFactorsDistinct(sq[i[0]], sq[i[1]]) for i in combinations(range(sq_len), 2)])

if __name__ == '__main__':
    i = 600
    loc = 4
    while i:
        tmp = []
        k = 0
        while k < loc:
            if primeFactorsNum(i+k) !=  loc:
                i += (k+1)
                k = 0
                continue
            else:
                k += 1
        for k in range(loc):
            i_f = factors(i+k)
            tmp.append(i_f)
        else:
            if isAllFactorsDistinct(tmp):
                print i
                i = 0
            else:
                i += loc
