# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s):
    n = len(s)

    dp = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        dp[i][i] = True
    p = s[i]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    if j - i + 1 > len(p):
                        p = s[i: j + 1]
    return p