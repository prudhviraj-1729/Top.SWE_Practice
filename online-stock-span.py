# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.stack = [(10**6, 1)]
        
    def next(self, price):
        if price < self.stack[-1][0]:
            self.stack.append([price, 1])
        else:
            count = 1
            while price >= self.stack[-1][0]:
                count += self.stack[-1][1]
                self.stack.pop()
            self.stack.append([price, count])
        return self.stack[-1][1]