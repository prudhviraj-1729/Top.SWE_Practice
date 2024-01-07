# https://leetcode.com/problems/copy-list-with-random-pointer/

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def copyRandomList(head):
    oldToCopy = {None: None}

    cur = head
    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next
    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
    return oldToCopy[head]