class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #Binary search method Time: O(nlog(sum(w) - max(w))) Space: O(1)
        l, r = max(weights), sum(weights)
        res = r

        def capneed(cap: int) -> bool:
            days_need = 1
            current_cap = cap

            for w in weights:
                if current_cap - w < 0:
                    days_need += 1
                    current_cap = cap
                
                current_cap -= w
            
            return days_need <= days

        while l <= r:
            mid = (l + r) // 2

            if capneed(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

        #Another Binary search method Time: O(nlog(sum(w) - max(w))) Space: O(1)
        # l, r = max(weights), sum(weights)
        # res = r

        # while l <= r:
        #     mid = (l + r) // 2
        #     needed_days = 1
        #     current_weight = 0

        #     for w in weights:
        #         if current_weight + w > mid:
        #             current_weight = 0
        #             needed_days += 1

        #         current_weight += w
            
        #     if needed_days > days:
        #         l = mid + 1
        #     else:
        #         res = mid
        #         r = mid - 1
        
        # return res