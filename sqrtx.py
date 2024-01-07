# https://leetcode.com/problems/sqrtx/

def mySqrt(x):
    if x <= 1:
        return x
    l, r = 0, x
    while l < r:
        mid = l + ((r - l) // 2)
        if mid * mid <= x:
            l = mid + 1
        else:
            r = mid
    return l - 1