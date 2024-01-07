# https://leetcode.com/problems/coin-change/

def coinChange(coins, amount):
    
    dp = [0] + [float("inf") for i in range(amount)]
    for coin in coins:
        for j in range(1, amount + 1):
            if coin <= j:
                dp[j] = min(dp[j], dp[j - coin] + 1)
    if dp[-1] == float("inf"):
        return -1
    return dp[-1]