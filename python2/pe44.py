from Euler import pentagonalNum

if __name__ == '__main__':
    i = 3
    while i > 1:
        s_ = i * (3*i - 1) // 2
        for j in range(1, i):
            pj = j * (3*j - 1) // 2
            if pentagonalNum(s_-pj) and pentagonalNum(s_-2*pj):
                print s_-2*pj
                i = 0
                break
        i += 1
