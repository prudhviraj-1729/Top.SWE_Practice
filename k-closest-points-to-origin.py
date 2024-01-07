# https://leetcode.com/problems/k-closest-points-to-origin/

from collections import heapq
import math

def kClosest(points, k):
    helper = []
    for x, y in points:
        dist = math.sqrt((x ** 2) + (y ** 2))
        helper.append([dist, x, y])
    heapq.heapify(helper)
    res = []
    for i in range(k):
        dist, x, y = heapq.heappop(helper)
        res.append([x, y])
    return res