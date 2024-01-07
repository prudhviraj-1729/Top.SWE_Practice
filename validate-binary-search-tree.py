# https://leetcode.com/problems/validate-binary-search-tree/

def isValidBST(root):
        
    def solve(node, left_node = -float("inf"), right_node = float("inf")):
        if not node:
            return True
        if left_node < node.val < right_node:
            return solve(node.left, left_node, node.val) and solve(node.right, node.val, right_node)
        else:
            return False

    return solve(root)