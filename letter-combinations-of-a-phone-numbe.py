# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(digits):
    
    res = []
    numToChar = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }

    def dfs(i, currStr):
        if len(currStr) == len(digits):
            res.append(currStr)
            return
        for c in numToChar[digits[i]]:
            dfs(i + 1, currStr + c)
    if digits:
        dfs(0, "")
    return res