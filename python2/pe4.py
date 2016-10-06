def isPalindrome(aint):
    tmp = ''
    while aint > 0:
        tmp = "{0}{1}".format(tmp, aint % 10)
        aint /= 10
    if tmp == tmp[::-1]:
        return True
    return False

def test():
    res = []
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            if isPalindrome(i * j):
                res.append((i, j, i*j))
    return res

if __name__ == '__main__':
    res = test()
    if res:
        res = sorted(res, lambda x, y: y[2] - x[2])
        print res[0]
    else:
        print 'Find nothing'
