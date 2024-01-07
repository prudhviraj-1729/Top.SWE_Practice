# https://leetcode.com/problems/longest-nice-subarray/

def longestNiceSubarray(nums):

    longest = 1
    i1 = 0
    n = len(nums)
    current = 0
    for i in range(n):
        while i1 < i and current & nums[i]:
            current ^= nums[i1]
            i1 += 1
        current |= nums[i]
        longest = max(longest, i-i1+1)

    return longest