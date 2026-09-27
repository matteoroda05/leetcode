from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # ordered_costs: List[int] = []

        # def insertionsort(value: int, ordered: List[int]) -> None:
        #     i = 0
        #     while i < len(ordered) and ordered[i] > value:
        #         i += 1
        #     ordered.insert(i, value)

        # for n, i in enumerate(cost):
        #     insertionsort(i, ordered_costs)

        cost.sort()
        out = 0
        i = len(cost) -1
        while i >= 0:#  len(ordered_costs):
            out += cost[i]

            if i - 1 >=0: # < len(ordered_costs):
                out += cost[i - 1]

            i-= 3

        return out