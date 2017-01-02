from itertools import permutations

def isLegal(sq):
    flag = [2, 3, 5, 7, 11, 13, 17]
    if sq[5] not in '05':
        return False
    for i in range(7):
        d = int(''.join(sq[i+1:i+4]))
        if d % flag[i] != 0:
            return False
    return True

if __name__ == '__main__':
    res = 0
    for i in permutations('0123456789'):
        if isLegal(i):
            res += int(''.join(i))
    print res
