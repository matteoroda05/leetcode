
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        out = Node(head.val) if head else None
        
        cur = head
        ncur = out
        oldToNew = {}
        while cur:
            oldToNew[cur] = ncur
            nxt = cur.next
            r = cur.random

            ncur.next = oldToNew[nxt] if nxt in oldToNew else (Node(nxt.val) if nxt else None)
            oldToNew[nxt] = ncur.next
            ncur.random = oldToNew[r] if r in oldToNew else (Node(r.val) if r else None)
            oldToNew[r] = ncur.random
            
            ncur = ncur.next
            cur = cur.next

        return out