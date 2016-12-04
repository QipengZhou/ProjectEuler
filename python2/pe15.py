def genTree(n_left, n_right, util_set={}):
    ans = 0
    if (n_left, n_right) in util_set:
        ans = util_set[(n_left, n_right)]
    elif (n_left == 1) or (n_right == 1):
        ans = (n_left + n_right)
    elif n_left == n_right:
        ans = 2 * genTree(n_left - 1, n_right, util_set)
    else:
        ans += genTree(n_left - 1, n_right, util_set)
        ans += genTree(n_left, n_right - 1, util_set)
    util_set[(n_left, n_right)] = ans
    return ans

if __name__ == '__main__':
    print 2*genTree(19, 20)

