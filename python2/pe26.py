def recipCyc(n):
    rem = [1]
    while True:
        a = rem[-1]
        flag = True
        while a < n:
            a *= 10
            if a in rem:
                return len(rem) - rem.index(a)
            if flag:
                flag = False
                continue
            rem.append(a)
        q, r = divmod(a, n)
        if r == 0:
            return 0
        elif r in rem:
            return len(rem) - rem.index(r)
        else:
            rem.append(r)

if __name__ == '__main__':
    a, b = 0, 0
    for i in range(2, 1000):
        n = recipCyc(i)
        if n > b:
            a, b = i, n
    print a
