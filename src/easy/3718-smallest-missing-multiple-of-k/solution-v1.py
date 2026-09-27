class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        found = False
        kMultiple = k

        while not found:
            if kMultiple not in nums:
                found = True
            else:
                kMultiple += k
        return kMultiple