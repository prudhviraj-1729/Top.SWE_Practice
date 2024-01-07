# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):

    max_upto_i = max_sum = nums[0]
    for i in range(1, len(nums)):
        max_upto_i = max(max_upto_i + nums[i], nums[i])
        max_sum = max(max_sum , max_upto_i)
    return max_sum