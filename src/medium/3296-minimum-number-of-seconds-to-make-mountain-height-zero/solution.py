import heapq

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """

        # [ (time, workerTime, times) ]
        pq = []
        for workerTime in workerTimes:
            cur = (workerTime, 1, workerTime)
            pq.append(cur)
        heapify(pq)

        res = 0

        for _ in range(mountainHeight):
            curTime, times, workerTime = heappop(pq)
            res = max(res, curTime)
            times+=1
            curTime += workerTime * times
            new = (curTime, times, workerTime)
            heappush(pq, new)
        
        return res
            



        
