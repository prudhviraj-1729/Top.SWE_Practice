# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    hashmap = {}

    i, j = 0, 0
    res = 0

    while j < len(s):
        if s[j] in hashmap:
            res = max(res, j - i)
            i = max(i, hashmap.get(s[j]) + 1)
        hashmap[s[j]] = j
        j += 1
    return max(res, j - i)