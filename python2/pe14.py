def collatz_seq(n):
    tmp = {}
    tmp[1] = [1]
    for i in range(2, n):
        if i in tmp:
            continue
        else:
            j = i
            utilSeq = []
            while (j != 1) and j not in tmp:
                utilSeq.append(j)
                if j % 2 == 0:
                    j /= 2
                else:
                    j = 3 * j + 1
            if j in tmp:
                tmp[i] = utilSeq + tmp[j]
            else:
                for k in range(len(utilSeq)):
                    if utilSeq[k] in tmp:
                        continue
                    else:
                        tmp[utilSeq[k]] = utilSeq[k:]
    return tmp

def collatz_num(n):
    tmp = {}
    tmp[1] = 1
    for i in range(2, n):
        if i in tmp:
            continue
        else:
            j = i
            utilSeq = []
            while j not in tmp:
                utilSeq.append(j)
                if j % 2 == 0:
                    j /= 2
                else:
                    j = 3 * j + 1
            mu = len(utilSeq)
            nu = tmp[j]
            for k in range(mu):
                tmp[utilSeq[k]] = nu + mu - k
    return tmp


if __name__ == '__main__':
    res = collatz_num(1000000)
    print max(res, key=lambda key: res[key])
