from Euler import triangleNum

if __name__ == '__main__':
    with open('p042_words.txt') as f:
        words = f.read().split(',')
    words_num = [map(lambda i: ord(i)-ord('A')+1, k.strip().strip('"'))
        for k in words]
    print sum([1 for i in words_num if triangleNum(sum(i))])
