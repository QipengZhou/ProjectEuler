def nameScores():
    res = 0
    with open('p022_names.txt') as f:
        i = 1
        lines = f.read().strip().split(',')
        lines.sort()
        for line in lines:
            tmp = 0
            for w in line.strip('"'):
                tmp += (ord(w) - ord('A') + 1)
            res += i * tmp
            i += 1
    return res

if __name__ == '__main__':
    print nameScores()
