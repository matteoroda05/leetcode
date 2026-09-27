from collections import deque
import heapq
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        heap = []
        heapify(heap)
        seen = {} # lake : last_index
        ans = [1] * len(rains)
        for i in range(len(rains)):
            if rains[i] > 0:
                ans[i] = -1
                if rains[i] in seen:
                    tmp = []
                    while heap and heap[0] < seen[rains[i]]:
                        tmp.append(heappop(heap))
                    if heap:
                        ans[heappop(heap)] = rains[i]
                    else:
                        return []
                    while tmp:
                        heappush(heap, tmp.pop())
                seen[rains[i]] = i
            else:
                if seen:
                    heappush(heap, i)
        return ans
