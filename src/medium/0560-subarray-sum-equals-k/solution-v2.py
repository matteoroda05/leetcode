class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        cursum = 0
        res = 0
        for n in nums:
            # sumj = k + sumi
            sums[cursum + k] +=1
            cursum += n
            res += sums.get(cursum, 0)
        return res


    '''
    FOLLOWUP: How would you adapt this approach if the problem required finding the longest subarray with sum k instead?


    only save the first time we see a cursum:
    def func(arr, k):
        sums = {k: -1}
        cursum = 0
        maxlen = 0
        for i, n in enumerate(nums):
            cursum += n 
            if cursum in sums: 
                maxlen = max(maxlen, i - sums[cursum])
                # if we want to return it we keep track of maxI and maxJ and then reurn arr[i:j]
            sums[cursum + k] = sums.get(cursum + k, i)
        return maxlen
    '''