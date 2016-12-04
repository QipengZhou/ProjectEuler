def weekNum(frtTurn, numDays):
    ans = 0
    while frtTurn <= numDays:
        frtTurn += 7
        ans += 1
    return ans

days30 = [4, 6, 9, 11]

def firstDayOfEachMonth(year, firstDay):
    ans = [firstDay]
    for i in range(1, 12):
        plusDay = 30
        if i == 2:
            plusDay = 28
            if Euler.isLeap(year):
                plusDay = 29
            ans.append((ans[i-1] + plusDay%7)%7)
            continue
        if i not in days30:
            plusDay = 31
        ans.append((ans[i-1] + plusDay%7)%7)
    return ans

if __name__ == '__main__':
    import Euler
    days = 365
    firstDay = 1
    ans = []
    for i in range(1901, 2001):
        firstDay = (firstDay + days % 7) % 7
        ans.append(firstDayOfEachMonth(i, firstDay))
    print sum([i.count(0) for i in ans])
