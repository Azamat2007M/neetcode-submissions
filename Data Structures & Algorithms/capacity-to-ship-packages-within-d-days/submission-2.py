class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            mid = (l + r) // 2
            days_mid = 1
            sum_mid = 0

            for w in weights:
                if sum_mid + w > mid:
                    sum_mid = 0
                    days_mid += 1

                sum_mid += w
            
            if days_mid > days:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        
        return res