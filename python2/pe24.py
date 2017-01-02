from itertools import permutations

if __name__ == '__main__':
    print ''.join(list(permutations('0123456789'))[1000000-1])
