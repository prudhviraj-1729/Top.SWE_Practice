# https://leetcode.com/problems/minimum-depth-of-binary-tree/

def minDepth(self, root):
    if not root:
        return 0
    left = self.minDepth(root.left)
    right = self.minDepth(root.right)
    if not left and not right:
        return 1
    if not left:
        return 1 + right
    if not right:
        return 1 + left
    return 1 + min(left, right)