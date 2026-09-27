class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]), reverse=True) # sort as tuple to have order also in second element
    
        out = []
        while intervals:
            x = intervals.pop()
            if out and out[-1][1] >= x[0]:
                out[-1][1] = x[1] if x[1] > out[-1][1] else out[-1][1]
            else:
                out.append(x)
            
        return out