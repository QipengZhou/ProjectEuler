def isSeqPandigital(sq):
    s = ''
    for i in sq:
        s += str(i)
        if len(s) >= 9:
            break
    if ''.join(sorted(s)) == '123456789':
        return int(s)
    else:
        return None

if __name__ == '__main__':
    res = 918273645
    for i in range(1, 5):
        if 2 * i > 9:
            continue
        flag = 9 / i
        ans = [[j*k for k in range(1, flag+1)] \
                for j in range(pow(10, i-1), pow(10, i))]
        for k in ans:
            a = isSeqPandigital(k)
            if a and a > res:
                res = a
    print res
