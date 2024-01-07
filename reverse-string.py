# https://leetcode.com/problems/reverse-string/

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]