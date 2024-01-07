# https://leetcode.com/problems/number-of-atoms/

from collections import Counter

def countOfAtoms(formula):
    stack, num, elem, Count = [1], "", "", Counter()
    for s in formula[::-1]:
        if s.isdigit():
            num += s
        elif s == ')':
            k = int(num[::-1]) * stack[-1] if num else 1
            stack.append(k)
            num = ''
        elif s == '(':
            stack.pop()
            num = ''
        elif s.isupper():
            elem += s
            k = int(num[::-1]) if num else 1
            Count[elem[::-1]] += stack[-1] * k
            elem, num = "", ""
        elif s.islower():
            elem += s
        
    return "".join(i + str(j)*(j!=1) for i,j in sorted(Count.items()))