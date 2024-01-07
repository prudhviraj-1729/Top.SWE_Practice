# https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
from itertools import accumulate

def subarraySum(nums, k):
    arr = [0] + list(accumulate(nums))
    d = defaultdict(int)
    count = 0
    for i in arr:
        if (i - k) in d:
            count += d[i - k]
        d[i] += 1
    return count