# https://leetcode.com/problems/binary-search/

def search(nums, target):
    
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return -1