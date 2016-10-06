import pe3

res = {}

for i in range(2, 21):
    tmp = pe3.factors(i)
    for j in tmp:
        if j not in res or res[j] < tmp[j]:
            res[j] = tmp[j]

print reduce(lambda x,y: x*y, map(lambda i: i**res[i], res))
