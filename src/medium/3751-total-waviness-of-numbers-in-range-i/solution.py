class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        out=0
        for i in range(num1, num2+1):
            num = str(i)
            for j, n in enumerate(num):
                if j == 0 or j == len(num) - 1: 
                    continue
                if (n > num[j-1] and n > num[j+1]) or (n < num[j-1] and n < num[j+1]):
                    out+=1
        return out