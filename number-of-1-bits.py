# https://leetcode.com/problems/number-of-1-bits/

def hammingWeight(n):
    return str(bin(n)).count('1')