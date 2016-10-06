def spytha(n):
    """ for special pythagorean triplet """
    res = []
    for i in range(1, n):
        for j in range(i+1, n):
            k = n - i - j
            if (k > j) and (i*i + j*j == k*k):
                res.append((i, j, k))
    return res

if __name__ == '__main__':
    print [reduce(lambda x,y: x*y, i) for i in spytha(1000)]
