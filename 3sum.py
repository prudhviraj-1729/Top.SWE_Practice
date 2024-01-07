# https://leetcode.com/problems/3sum/

def threeSum(nums):
        
    nums = sorted(nums)
    res = []

    for i, a in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            target = a + nums[l] + nums[r]
            if target < 0:
                l += 1
            elif target > 0:
                r -= 1
            else: 
                res.append([a, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res