class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = list(list())
        done = set()
        tdone = set()
        
        for i, num in enumerate(nums):
            if num in done:
                continue
            
            done.add(num)
            tSum = self.twoSum(nums, -num, i)
            if tSum:
                for l in tSum:
                    l.append(num)
                    l.sort()
                    t = tuple(l)
                    if t not in tdone:
                        out.append(l)
                        tdone.add(t)
        return out

    def twoSum(self, nums: list[int], target: int, dont: int) -> list[list[int]]:
        prefix = {}
        lists = list(list())
        for i, num in enumerate(nums[dont+1:]):
            if num in prefix:
                lists.append([num, prefix[num]])
            
            prefix[target - num] = num
        
        return lists