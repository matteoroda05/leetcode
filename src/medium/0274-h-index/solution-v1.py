class Solution:
    def hIndex_logarithmic(self, citations: list[int]) -> int:
        citations.sort(reverse = True)
        hIndex, sizeof = 0, len(citations)
        for i, n in enumerate(citations):
            candidate = min(n, i+1)
            if candidate > hIndex:
                hIndex = candidate
        return hIndex
    
    def hIndex(self, citations: list[int]) -> int:
        cnt = Counter(citations)
        c,h = 0,0
        for n, count in sorted(cnt.items(), reverse = True):
            c += count
            h = max(min(c,n), h)
            if c >= n and n > 0:
                h = max(n, h)
        return h
        