# https://leetcode.com/problems/kth-largest-element-in-an-array/

from collections import heapq

def findKthLargest(nums, k):
    nums.sort()
    return nums[len(nums) - 1 - k]

def findKthLargest(nums, k):
    maxheap = []
    for i in nums:
        heapq.heappush(maxheap, -1 * i)
    for i in range(k - 1):
        heapq.heappop(maxheap)
    return -1 * heapq.heappop(maxheap)

def findKthLargest(nums, k):
    k = len(nums) - k
    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k: return quickSelect(l, p - 1)
        elif p < k: return quickSelect(p + 1, r)
        else:
            return nums[p]
    return quickSelect(0, len(nums) - 1)