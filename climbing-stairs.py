# https://leetcode.com/problems/climbing-stairs/

def climbStairs(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]