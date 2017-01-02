from Euler import triangleNum, pentagonalNum

if __name__ == '__main__':
    i = 144
    while True:
        h = i * (2 * i - 1)
        if triangleNum(h) and pentagonalNum(h):
            print h
            break
        else:
            i += 1
