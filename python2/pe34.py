if __name__ == '__main__':
    factVal = {'0': 1}
    ans = 1
    for i in range(1, 10):
        ans *= i
        factVal[str(i)] = ans
    res = []
    for i in range(2, 10):
        if pow(10, i) > i * factVal['9']:
            break
        ta = [sum(map(lambda j: factVal[j], str(k))) for k in range(pow(10, i-1), pow(10, i))]
        tb = range(pow(10, i-1), pow(10, i))
        for j in range(len(ta)):
            if ta[j] == tb[j]:
                res.append(ta[j])
    print sum(res)
