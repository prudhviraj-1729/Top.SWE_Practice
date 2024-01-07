# https://leetcode.com/problems/daily-temperatures/

def dailyTemperatures(arr):
    res = [0] * len(arr)
    stack = []
    for i, t in enumerate(arr):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append([t, i])
    return res