# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if all([l1, l2]) is None:
            return None
        if any([l1, l2]) is None:
            return l1 if l1 else l2

        out = ListNode()

        co = out
        r = 0
        c1, c2 = l1, l2
        while c1 or c2 or r != 0:
            co.next = ListNode()
            co = co.next
            if c1 and c2:
                s = c1.val + c2.val + r
                co.val = s%10
                r = 1 if s >= 10 else 0

                c1 = c1.next
                c2 = c2.next
            elif c1:
                s = c1.val + r
                co.val = s%10
                r = 1 if s>=10 else 0
                
                c1 = c1.next
            elif c2:
                s = c2.val + r
                co.val = s%10
                r = 1 if s>=10 else 0
            
                c2 = c2.next
            else: 
                co.val = r
                r = 0
        return out.next