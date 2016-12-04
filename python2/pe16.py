if __name__ == '__main__':
    tmp = str(2 ** 1000)
    ans = 0
    for i in tmp:
        ans += int(i)
    print ans
