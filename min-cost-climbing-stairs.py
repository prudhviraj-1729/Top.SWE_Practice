# https://leetcode.com/problems/min-cost-climbing-stairs/

def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [-1 for j in range(n + 1)]
    def solve(cost, n):
        if n <= 1:
            return cost[n]
        if dp[n] != -1:
            return dp[n]
        dp[n] = cost[n] + min(solve(cost, n - 1), solve(cost, n - 2))
        return dp[n]
        
    return min(solve(cost, n - 1), solve(cost, n - 2))