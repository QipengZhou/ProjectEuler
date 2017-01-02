def getNDigit(n):
    c_count = 0
    for i in range(1, n+1):
        i_str = str(i)
        c_count += len(i_str)
        if c_count < n:
            continue
        return int(i_str[len(i_str)-(c_count-n)-1])

if __name__ == '__main__':
    res = 1
    for i in range(7):
        res *= getNDigit(pow(10, i))
    print res
