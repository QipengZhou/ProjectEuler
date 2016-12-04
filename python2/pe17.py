def num2words(n):
    num = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
           7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
           12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
           16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
           20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
           70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred',
           1000: 'thousand'}

    if (n == 1000) or (n == 100):
        return 'one ' + num[n]

    if n in num:
        return num[n]
    if n > 1000:
        raise ValueError('the number cannot support greater than 1000')

    ans = ''

    if n >= 100 and n < 1000:
        h = n / 100
        ans += num[h] + ' hundred'
        n = n % 100

    if n > 0 and n < 100:
        if n in num:
            ans += (num[n] if not ans else ' and {0}'.format(num[n]))
        else:
            j = n % 10
            tmp = "{0}-{1}".format(num[n-j], num[j])
            ans += (tmp if not ans else ' and {0}'.format(tmp))

    return ans

def numWordsLen(i):
    return len(i.replace(' ', '').replace('-', ''))

if __name__ == '__main__':
    print sum([numWordsLen(num2words(i)) for i in range(1, 1001)])
