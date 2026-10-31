class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0
        M = 0
        
        # [0, 1] 
        for i, n in enumerate(arr):
            if i == M and n <= M:
                chunks += 1
                M += 1
                continue
            if n > M: 
                M = n
        return chunks