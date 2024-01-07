# https://leetcode.com/problems/symmetric-tree/

def isSymmetric(root):

    def isSameTree(p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
        else:
            return False
    if not root:
        return True
    p = root.left
    q = root.right
    return isSameTree(p, q)