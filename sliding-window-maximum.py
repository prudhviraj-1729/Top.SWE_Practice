# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque

def maxSlidingWindow(nums, k):
        
    i, j = 0, 0
    res = []
    q = deque()

    while j < len(nums):
        while q and nums[j] >= nums[q[-1]]:
            q.pop()
        q.append(j)

        if j - i + 1 < k :
            j += 1
        elif j - i + 1 == k:
            res.append(nums[q[0]])
            if q[0] == i:
                q.popleft()
            i += 1
            j += 1
    return res