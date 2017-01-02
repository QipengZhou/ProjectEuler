from Euler import properDivisors

if __name__ == '__main__':
    res = []
    for a in range(2, 10000):
        if a not in res:
            b = sum(properDivisors(a))
            if a != b:
                db = sum(properDivisors(b))
                if a == db:
                    res.append(a)
                    if b not in res:
                        res.append(b)
    print sum(res)
