# https://leetcode.com/problems/first-bad-version/

# Function which returns whether it is a bad version of not
def isBadVersion(n):
    return 

def firstBadVersion(n):
    l, r = 1, n + 1
    while l < r:
        mid = l + (r - l) // 2
        if not isBadVersion(mid):
            l = mid + 1
        else:
            r = mid 
    return l