# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys

def maxProfit(prices):
    min_val = sys.maxsize
    dp = [0 for j in range(len(prices))]

    for i in range(len(prices)):
        min_val = min(min_val, prices[i])
        dp[i] = max(prices[i] - min_val, dp[i - 1])
    return dp[-1]