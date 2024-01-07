# https://leetcode.com/problems/lfu-cache/

from collections import defaultdict

class ListNode:
    def __init__(self, key = None, val=0, freq = 1, nxt=None, prv=None):
        self.val = val
        self.key = key
        self.next = nxt
        self.prev = prv
        self.freq = freq

class DList:
    def __init__(self):
        self.head = ListNode() # dummy node
        self.head.next = self.head.prev = self.head
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        self._size += 1
    
    def pop(self, node=None):
        if self._size == 0: return
        
        if not node: node = self.head.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        
        return node

class LFUCache:

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._node = dict() # key: Node
        self._freq = defaultdict(DList)
        self._minfreq = 0 
        
    def _update(self, node):
        freq = node.freq
        
        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)
    
    def get(self, key):
        if key not in self._node: return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
                
            node = ListNode(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1