from collections import defaultdict

def coinSum(coins, coin):
    tmp = sorted(coins, reverse=True)
    ans = [coin]
    res = 0
    for i in tmp:
        tt = []
        while ans:
            a = ans.pop()
            for k in range(a/i+1):
                if i*k == a:
                    res += 1
                else:
                    tt.append(a - i*k)
        ans.extend(tt)
    return res

if __name__ == '__main__':
    print coinSum([1, 2, 5, 10, 20, 50, 100, 200], 200)
