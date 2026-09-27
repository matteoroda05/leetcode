class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        gains = [0]

        cmax, cmin, gain = 0, inf, 0
        for p in prices: 
            if p < cmin:
                cmin = p
                cmax = p
                gains.append(gain)
                continue
            cmax = p if p>cmax else cmax
            gain = cmax-cmin if cmax-cmin > gain else gain
            gains.append(gain)

        cmax, cmin, gain = 0, inf, 0
        size=len(gains)
        for i, p in enumerate(reversed(prices)):
            p = -p
            if p < cmin:
                cmin = p
                cmax = p
                gains.append(gain)
                continue
            cmax = p if p>cmax else cmax
            gain = cmax-cmin
            gains[size-2-i] += abs(gain)

        return max(gains)