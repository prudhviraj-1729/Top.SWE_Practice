# https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    
    minStr = min(strs, key=len)
    for i in range(len(strs)):
        while not strs[i].startswith(minStr):
            minStr = minStr[:- 1]
    return minStr