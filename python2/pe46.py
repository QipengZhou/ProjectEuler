from Euler import isPrime

def isOddOk(n):
    i = 1
    t = n - 2 * pow(i, 2)
    while t > 1:
        if isPrime(t):
            return True
        i += 1
        t = n - 2 * pow(i, 2)
    return False

if __name__ == '__main__':
    i = 5
    while True:
        n = 2*i - 1
        if not isPrime(n) and not isOddOk(n):
            print n
            break
        i += 1
