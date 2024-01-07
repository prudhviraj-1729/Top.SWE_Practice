# https://leetcode.com/problems/max-consecutive-ones-iii/

def longestOnes(nums, k):
    i, j = 0, 0
    res = 0
    count = 0

    while j < len(nums):
        if nums[j] == 0:
            count += 1
        if count > k:
            if nums[i] == 0:
                count -= 1
            i += 1
        res = max(res, j - i + 1)
        j += 1
    return res