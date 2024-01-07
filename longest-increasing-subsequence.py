# https://leetcode.com/problems/longest-increasing-subsequence/

import bisect

def lengthOfLIS(nums):
    
    dp = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > dp[-1]:
            dp.append(nums[i])
        else:
            idx = bisect.bisect_left(dp, nums[i])
            dp[idx] = nums[i]
    return len(dp)