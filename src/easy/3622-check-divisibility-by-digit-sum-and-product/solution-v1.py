class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = []
        o = n

        while n > 0:
            digit = n % 10
            digits.append(digit)
            n = n // 10 
        
        totsum = sum(digits)

        if totsum > o:
            return False
        
        totmul = math.prod(digits)

        if o % (totmul + totsum) == 0:
            return True

        return False