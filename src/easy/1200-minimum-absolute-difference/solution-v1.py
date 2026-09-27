class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = arr[1]-arr[0]
        result = [[arr[0], arr[1]]]
        for i in range (1, len(arr) - 1) :
            tmp = arr[i+1] - arr[i]
            if tmp < min_diff:
                # Found a NEW smaller gap
                min_diff = tmp
                result = [[arr[i], arr[i+1]]]
            elif tmp == min_diff:
                # Found another pair with the same gap
                result.append([arr[i], arr[i+1]])
        return result
        