import random
class RandomizedSet:

    def __init__(self):
        self.tokey = {}
        self.toval = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        k = self.tokey.get(val, -1)
        if k != -1:
            return False
        self.tokey[val] = self.size
        self.toval[self.size] = val
        self.size +=1
        return True

    def remove(self, val: int) -> bool:
        k = self.tokey.get(val, -1)
        if k == -1:
            return False
        
        self.size -=1
        self.toval[k] = self.toval[self.size]
        self.tokey[self.toval[k]] = k
        del self.tokey[val]
        del self.toval[self.size]

        return True
        
    def getRandom(self) -> int:
        return self.toval[random.randrange(self.size)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()