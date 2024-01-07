# https://leetcode.com/problems/binary-search-tree-iterator/

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.curr = root
        
    def next(self):
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        self.curr = self.stack.pop()
        out = self.curr.val
        self.curr = self.curr.right
        return out

    def hasNext(self):
        return self.stack or self.curr