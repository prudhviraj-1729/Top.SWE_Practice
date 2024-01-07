# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

def minAddToMakeValid(s):
    
    lft = [0]
    for c in s:
        lft += [lft[-1] + (c == "(") - (c == ")")]
        
    rgh = [0]
    for c in s[::-1]:
        rgh += [rgh[-1] + (c == ")") - (c == "(")]
        
    return -min(min(lft), 0) - min(min(rgh), 0)