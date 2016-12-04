def reduceNum(n, a):
    while n % a == 0:
        n /= a
    return n

if __name__ == '__main__':
    ans = 1
    for i in range(2, 101):
        ans = reduceNum(ans * i, 10)
    print sum([int(i) for i in str(ans)])
