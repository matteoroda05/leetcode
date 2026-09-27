class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        a, b = 0, 0
        isAlice = True
        while piles:
            if piles[0] > piles[len(piles)-1]:
                toAdd = piles.pop(0)
                if isAlice:
                    a += toAdd
                else:
                    b += toAdd
            elif piles[0] < piles[len(piles)-1]:
                toAdd = piles.pop()
                if isAlice:
                    a += toAdd
                else:
                    b += toAdd
            else: 
                if piles[1] > piles[len(piles)-2]:
                    toAdd = piles.pop(0)
                    if isAlice:
                        a += toAdd
                    else:
                        b += toAdd
                else: # piles[1] < piles[len(piles)-2]:
                    toAdd = piles.pop()
                    if isAlice:
                        a += toAdd
                    else:
                        b += toAdd
        return a > b