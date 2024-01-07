# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target):

    res = []
    subset = []
    def dfs(i, subset, total):
        if total == target:
            res.append(subset.copy())
            return
        if i >= len(candidates) or total > target:
            return
        subset.append(candidates[i])
        dfs(i, subset, total + candidates[i])
        subset.pop()
        dfs(i + 1, subset, total)

    dfs(0, subset, 0)
    return res