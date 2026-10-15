class Solution:
    def reverse(self, x: int) -> int:
        o = 0
        sign = (x < 0)
        x = abs(x)
        while x > 0:
            o = o*10 + x%10
            x = x // 10
        o = -o if sign else o

        if o > 2**31 -1 or o < -2**31:
            return 0
        return o