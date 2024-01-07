# https://leetcode.com/problems/middle-of-the-linked-list/

def middleNode(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow