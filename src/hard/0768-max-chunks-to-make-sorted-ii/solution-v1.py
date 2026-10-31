class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
      maxime = []
      M = float("-inf")
      
      for n in arr:
        M = M if M > n else n
        while maxime and maxime[-1] > n:
          maxime.pop(-1)
        maxime.append(M)
        
      return len(maxime)
      
        