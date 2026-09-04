class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            mid = (l + r) // 2
            needed_days = 1
            current_weight = 0

            for w in weights:
                if current_weight + w > mid:
                    current_weight = 0
                    needed_days += 1

                current_weight += w
            
            if needed_days > days:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        
        return res