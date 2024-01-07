# https://leetcode.com/problems/random-pick-with-weight/

import random

def __init__(self, w):
    self.w = w
    l = len(self.w)
    sum_w = sum(self.w)
    for i in range(l):
        self.w[i]/= sum_w
    for i in range(1, l):
        self.w[i] += self.w[i-1]  

def pickIndex(self) -> int:
    n = random.uniform(0,1)
    index = -1
    while True:
        index += 1
        if n <= self.w[index]:
            break
    return index