# https://leetcode.com/problems/group-anagrams/

import collections

def groupAnagrams(strs):

    res = collections.defaultdict(lambda:list())
    for word in strs:
        count = [0] * 26
        for letter in word:
            count[ord(letter) - ord("a")] += 1
        res[tuple(count)].append(word)
    return res.values()