# https://leetcode.com/problems/word-break/

def wordBreak(s, wordDict):
    #Using two for loops
    n = len(s)
    dp = [False for i in range(n + 1)]
    dp[0] = True

    for i in range(n):
        for j in range(i, n + 1):
            if dp[i] and s[i : j] in wordDict:
                dp[j] = True
    return dp[n]

    #A More efficient way
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False for i in range(n + 1)]
    dp[0] = True
    max_len_word = max(wordDict, key = len)

    for i in range(1, n + 1):
        for j in range(i - 1, max(i - len(max_len_word) - 1, -1), -1):
            if dp[j] and s[j : i] in wordDict:
                dp[i] = True
                break
    return dp[n]