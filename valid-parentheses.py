# https://leetcode.com/problems/valid-parentheses/

def isValid(s):

    map = {"}":"{", "]":"[",")":"("}
    stack = []
    for i in s:
        if i not in map:
            stack.append(i)
            continue
        if not stack or stack[-1] != map[i]:
            return False
        stack.pop()
    return not stack