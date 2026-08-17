from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Method Neetcode with Hashmap Time: O(n) Space: O(1)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue
            
            new_dict = defaultdict(int)

            for n, f in count.items():
                if f > 1:
                    new_dict[n] = f - 1
            
            count = new_dict
        
        res = []

        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res

        # Method Boyera-Mura algorithm Time: O(n) Space: O(1)
        # cand1, cand2 = None, None
        # count1, count2 = 0, 0 

        # for num in nums:
        #     if cand1 == num:
        #         count1 += 1
        #     elif cand2 == num:
        #         count2 += 1
        #     elif count1 == 0:
        #         cand1 = num
        #         count1 = 1
        #     elif count2 == 0:
        #         cand2 = num
        #         count2 = 1
        #     else:
        #         count1 -= 1
        #         count2 -= 1
            
        # res = []
        # n = len(nums)

        # for cand in (cand1, cand2):
        #     if cand is not None and nums.count(cand) > n // 3:
        #         res.append(cand)

        # return res
