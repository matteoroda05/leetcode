class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        out = 0
        for prev, cur in zip(prices, prices[1:]):
            if prev < cur:
                out += cur-prev
        return out