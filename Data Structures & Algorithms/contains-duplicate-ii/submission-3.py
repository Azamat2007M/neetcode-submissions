class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Slidding window method Time: O(n) Space: O(k)
        window = set()
        j = 0

        for i in range(len(nums)):
            if i - j > k:
                window.remove(nums[j])
                j += 1
            if nums[i] in window:
                return True
            
            window.add(nums[i])

        return False

        #Anothe method Hash Map Time: O(n) Space: O(k)
        # seen = {}

        # for i, num in enumerate(nums):
        #     if num in seen and i - seen[num] <= k:
        #         return True
            
        #     seen[num] = i

        # return False