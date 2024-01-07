# https://leetcode.com/problems/house-robber/

def rob(nums):
    dp = [-1 for j in range(len(nums))]
    def solve(arr, n):
        if n <= 0:
            return arr[n]
        if n == 1:
            return max(arr[n], arr[n - 1])
        if dp[n] != -1:
            return dp[n]
        dp[n] = max(arr[n] + solve(arr, n - 2), solve(arr, n -1))
        return dp[n]
    res = solve(nums, len(nums) - 1)
    return res

def rob(nums):
    n = len(nums)
    dp = [0 for j in range(n)]
    def solve(a, n):
        dp[0] = a[0]
        if n >= 1:
            dp[1] = max(a[0], a[1])
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], a[i] + dp[i - 2])
        return dp[n]
    res = solve(nums, n - 1)
    return res