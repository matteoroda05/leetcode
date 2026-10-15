class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxgain = 0
        minprice = prices[0]
        maxprice = prices[0]

        for n in prices:
            if n < minprice:
                minprice = n
                maxprice = n
            elif n > maxprice:
                maxprice = n
            if maxgain < maxprice-minprice:
                maxgain = maxprice-minprice

        return maxgain