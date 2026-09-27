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

        # while i<=j and j < size -1:
        #     while prices[i] > prices[i+1]:
        #         i+=1
        #         j+=1
        #         minprice = prices[i] if prices[i]<minprice else minprice
        #     while prices[j] < prices[j+1]:
        #         j+=1
        #         maxgain = prices[j] - minprice if prices[j] - minprice > maxgain else maxgain

        # return maxgain