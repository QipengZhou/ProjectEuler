def fib(n):
    a, b = 1, 2
    while a <= n:
        a, b = b, a+b
        yield b - a

if __name__ == '__main__':
    s = 0
    for i in fib(4000000):
        if i % 2 == 0:
            s += i
    print s
