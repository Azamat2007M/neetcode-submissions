import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Binary Search method Time: O(nlog(max(p))) Space: O(1)
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hour = sum(math.ceil(p / k) for p in piles)

            if hour <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
