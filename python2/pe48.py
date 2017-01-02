def selfPowers(n, nth):
    res = 0
    for i in range(1, n+1):
        tmp = 1
        for k in range(i):
            tmp *= i
            tmp %= pow(10, nth)
            if tmp == 0:
                break
        else:
            res += tmp
            res %= pow(10, nth)
    return res

if __name__ == '__main__':
    print selfPowers(1000, 10)
