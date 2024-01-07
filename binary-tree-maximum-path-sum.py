# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

def maxPathSum(root):
        
    res = root.val

    def diameter(node):
        nonlocal res
        if not node:
            return 0
        left_dia = max(0, diameter(node.left))
        right_dia = max(0, diameter(node.right))
        res = max(res, left_dia + right_dia + node.val)

        return max(left_dia, right_dia) + node.val
    
    diameter(root)
    return res