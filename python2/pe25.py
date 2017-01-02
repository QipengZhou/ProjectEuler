if __name__ == '__main__':
    f1 = 1
    f2 = 1
    i = 2
    while len(str(f2)) < 1000:
        i += 1
        f1, f2 = f2, f1 + f2
    print i
