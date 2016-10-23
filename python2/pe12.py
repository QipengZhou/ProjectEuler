import Euler

request = 500
if __name__ == '__main__':
    i = 6000
    while True:
        triNum = Euler.triangleNum(i)
        if Euler.factorNum(triNum) > request:
            print triNum
            break
        i += 1
