import math

def sieveErato(n):
    flag = [1] * (n + 1)
    flag[0] = 0
    flag[1] = 0
    for i in range(2, int(math.sqrt(n))+1):
        if flag[i]:
            for j in range(i*i, n+1, i):
                flag[j] = 0
    return flag

loc = 10001
n = 100000
res = sieveErato(n)
while sum(res) < loc:
    n *= 2
    res = sieveErato(n)

i = 0
j = 0
while i < loc:
    j += 1
    if res[j]:
        i += 1
print j
