class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        out = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], interval[1])
            else:
                out.append(interval)
        return out