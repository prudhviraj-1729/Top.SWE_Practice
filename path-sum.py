# https://leetcode.com/problems/path-sum/

def hasPathSum(root, targetSum):
        
    def pathSum(node, x):
        if not node.left and not node.right: return x == node.val
        if node.left and pathSum(node.left, x - node.val): return True
        if node.right and pathSum(node.right, x - node.val): return True
        return False

    if not root:
        return False
    return pathSum(root, targetSum)