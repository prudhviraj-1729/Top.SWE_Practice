# https://leetcode.com/problems/range-sum-query-immutable/

from itertools import accumulate

def __init__(self, nums):
    self.arr = [0] + list(accumulate(nums))
    
def sumRange(self, left, right):
    return self.arr[right + 1] - self.arr[left]