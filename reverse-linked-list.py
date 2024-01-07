# https://leetcode.com/problems/reverse-linked-list/

def reverseList(head):

    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev