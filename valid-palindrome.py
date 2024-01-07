# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not(s[l].isdigit()) and not(s[l].isalpha()):
            l += 1
        elif not(s[r].isdigit()) and not(s[r].isalpha()):
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
    return True

