# https://leetcode.com/problems/maximum-product-subarray/

def maxProduct(nums):

    numsrev = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        numsrev[i] *= numsrev[i - 1] or 1
    return max(nums + numsrev)