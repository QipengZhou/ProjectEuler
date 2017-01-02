from Euler import gcd

if __name__ == '__main__':
    ans = []
    for i in range(11, 100):
        for j in range(i+1, 100):
            ia, ib = i / 10, i % 10
            ja, jb = j / 10, j % 10
            if ib == ja and (i*jb == j* ia):
                ans.append((ia,jb))
    a, b = reduce(lambda x, y: (x[0]*y[0], x[1]*y[1]), ans, (1,1))
    print b/gcd(a,b)
