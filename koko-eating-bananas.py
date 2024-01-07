# https://leetcode.com/problems/koko-eating-bananas/

def minEatingSpeed(piles, h):

    def isPossible(speed):
        sum = 0
        for pile in piles:
            sum = sum + (pile - 1) // speed + 1
        return sum <= h

    l, r = 1, max(piles)
    while l < r:
        mid = l + (r - l) // 2
        if isPossible(mid):
            r = mid
        else:
            l = mid + 1
    return l