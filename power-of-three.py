# https://leetcode.com/problems/power-of-three/

def isPowerOfThree(n):

    temp = 1
    while n > 1 and temp < n:
        temp += temp << 1
    return temp == n
