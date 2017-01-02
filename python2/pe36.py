from Euler import genPalindromics

def dbasePalindromes(n):
    ans = []
    for i in genPalindromics(1, n):
        i2 = bin(i)[2:]
        if i2 == i2[::-1]:
            ans.append(i)
    return ans

if __name__ == '__main__':
    print sum(dbasePalindromes(pow(10, 6)))
