# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque

def levelOrder(root):
        
    res = []

    queue = deque()

    if root:
        queue.append(root)
    
    while queue:
        val = []
        for i in range(len(queue)):
            node = queue.popleft()
            val.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(val)
    
    return res