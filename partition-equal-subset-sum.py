# https://leetcode.com/problems/partition-equal-subset-sum/

def canPartition(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    if sum % 2 != 0:
        return False
    sum = sum // 2
    dp = [[0 for i in range(sum + 1)] for i in range(len(nums) + 1)]

    for i in range(len(nums) + 1):
        for j in range(sum + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True

    for i in range(1, len(nums) + 1):
        for j in range(1, sum + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[i][j]