# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    
    l, r = 0, len(height) - 1
    res = 0
    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l = l + 1
        else:
            r = r - 1
    return res
    