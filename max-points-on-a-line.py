# https://leetcode.com/problems/max-points-on-a-line/

from collections import Counter
from collections import defaultdict
from math import gcd

def maxPoints(points):

    points = list(Counter((x, y) for x, y in points).items())
    n = len(points)
    if n < 3: return sum(i for _,i in points)
    lines = defaultdict(set)
    
    for i in range(n):
        for j in range(i+1, n):
            (x1, y1), c1 = points[i]
            (x2, y2), c2 = points[j]
            a, b, c = y1 - y2, x2 - x1, x1*y2 - x2*y1
            d = gcd(gcd(a, b), c)
            a, b, c = a//d, b//d, c//d
            if a < 0 or a == 0 and b < 0: a, b, c = -a, -b, -c
            lines[a, b, c] |= set([i,j])

    return max(sum(points[i][1] for i in dr) for dr in lines.values())