from Euler import sieveErato, factors

def distinctPowers(b):
    res = []
    ans = []
    primes_ = sieveErato(b+1)
    for i in range(2, b+1):
        if i in primes_:
            res.append({i: 1})
        else:
            res.append(dict(factors(i)))
    for i in range(2, b+1):
        for j in res:
            tmp = {k: v*i for (k, v) in j.items()}
            if tmp not in ans:
                ans.append(tmp)
    return len(ans)

if __name__ == '__main__':
    print distinctPowers(100)
