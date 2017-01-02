from Euler import sieveErato, isPrime

def consecPrimeSum(lim_):
    tmp = sieveErato(lim_)
    tmp_len = len(tmp)
    rv_, rl_ = 0, 1

    for i in range(tmp_len):
        j_ran = range(i+rl_, tmp_len)
        iv_, il_ = rv_, rl_
        for j in j_ran:
            a = sum(tmp[i:j])
            if a >= lim_:
                if j == j_ran[0]:
                    return rv_, rl_
                break
            if isPrime(a):
                iv_, il_ = a, j - i
        if il_ > rl_:
            rv_, rl_ = iv_, il_
    return rv_, rl_

if __name__ == '__main__':
    print consecPrimeSum(pow(10, 6))
