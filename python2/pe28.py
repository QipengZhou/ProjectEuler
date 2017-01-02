if __name__ == '__main__':
    res = 1
    for i in range(2, 502):
        t = 2*i - 1
        res += (4*t*t - 6*t + 6)
    print res
