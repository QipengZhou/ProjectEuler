if __name__ == '__main__':
    ans = []
    for i in range(2, 10000):
        si = str(i)
        sil = len(si)
        a = pow(10, 4 - sil)
        for j in range(a, a*10):
            sj = str(j)
            ij = i * j
            sij = str(ij)
            if ij not in ans and ''.join(sorted(si+sj+sij))=='123456789':
                ans.append(ij)
    print sum(ans)
