# https://leetcode.com/problems/count-number-of-nice-subarrays/

def numberOfSubarrays(nums, k):
    
    prefix = {}
    countodd = 0
    res = 0

    for i in range(len(nums)):
        prefix[countodd] = prefix.get(countodd,0) + 1
        if nums[i]&1:
            countodd +=1
        if countodd >= k:
            x = countodd-k
            res += prefix[x]
            
    return res