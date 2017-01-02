def digitPower(nth):
    i = 2
    ans = []
    while True:
        a = pow(10, i-1)
        b = i*pow(9, nth)
        if b <= a:
            break
        b = min(pow(10, i) - 1, b)
        i += 1
        ans.extend(powerNum(a, b, nth))
    return ans

def powerNum(a, b, nth):
    res = []
    tmp = [sum(map(lambda i: pow(int(i), nth), str(k))) for k in range(a, b+1)]
    tt = range(a, b+1)
    for i in range(len(tt)):
        if tt[i] == tmp[i]:
            res.append(tt[i])
    return res

if __name__ == '__main__':
    print sum(digitPower(5))
