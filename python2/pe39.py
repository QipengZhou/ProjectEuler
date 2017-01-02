def rightTriples(p):
    ans = []
    for a in range(1, p/3+1):
        a1 = p * (p - 2*a)
        a2 = 2 * (p - a)
        if a1 % a2 == 0:
            b = a1 / a2
            if b <= a:
                break
            ans.append([a, b, p-(a+b)])
    return ans

if __name__ == '__main__':
    mp = 120
    mn = 3
    for i in range(1001):
        tmp = rightTriples(i)
        if len(tmp) > mn:
            mn = len(tmp)
            mp = i
    print mp, mn

