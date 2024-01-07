# https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    
    l, r = 0, len(height) - 1
    lm = height[l]
    rm = height[r]
    res = 0
    while l < r:
        if lm < rm:
            l = l + 1
            lm = max(lm, height[l])
            res = res + lm - height[l]
        else:
            r = r - 1
            rm = max(rm, height[r])
            res = res + rm - height[r]
    return res