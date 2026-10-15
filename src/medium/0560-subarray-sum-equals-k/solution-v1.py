class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = {k: 1}
        counter = 0
        summing = 0
        for i, n in enumerate(nums):
            summing += n
            counter += prefix.get(summing, 0)
            prefix[k+summing] = prefix.get(k+summing, 0) + 1

        return counter


    def subarraySumQuadratic(self, nums: List[int], k: int) -> int:
        '''
        brute force:
        - for every possible subarray O(n**n) check (not feasible)
        
        better idea: 
        - for every element obtain the sum to its right by using a hash map where we insert for every element == O(n) spatial and O(n**2) time
        - for every element in the hash check from the left how many values it can subtract from it to make it reach k == O(n**2)
        '''

        rightSum = {}

        for i, n in enumerate(nums):
            for j in range(0, i):
                rightSum[j] += n
            rightSum[i] = n
        
        rightSum[len(nums)]= 0
        
        # now the values are correctly 

        counter = 0
        for i in range(0, len(nums)):
            for j in range(len(nums),i,-1):
                if rightSum[i] - rightSum[j] == k:
                    counter +=1
        return counter