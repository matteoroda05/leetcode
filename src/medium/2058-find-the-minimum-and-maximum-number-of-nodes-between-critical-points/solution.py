class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        curIdx = 1
        cur = head
        criticals = []
        minDist = inf

        while cur.next:
            if prev and ((prev < cur.val and cur.next.val < cur.val) or (prev > cur.val and cur.next.val > cur.val)):
                if criticals and curIdx - criticals[-1] < minDist:
                    minDist = curIdx - criticals[-1]
                criticals.append(curIdx)
                
            prev = cur.val
            curIdx +=1
            cur = cur.next

        out = [-1,-1]
        if len(criticals) > 1:
            out[1] = criticals[-1] - criticals[0]
            out[0] = minDist
        return out
        
