from collections import defaultdict
from Euler import sieveErato

if __name__ == '__main__':
    tmp = sieveErato(1000000)
    res = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
    ans = defaultdict(list)
    for i in tmp:
        if i < 100:
            continue
        i_str = str(i)
        if '0' in i_str or '2' in i_str or '5' in i_str:
            continue
        ans[len(i_str)].append(i)

    for i in ans:
        tmp = ans[i]
        for k in tmp:
            if k in res:
                continue
            si = str(k)
            tt = set([int(si[j:]+si[:j]) for j in range(len(si))])
            for j in tt:
                if j in tmp:
                    continue
                break
            else:
                res.extend(tt)
    print len(res)
