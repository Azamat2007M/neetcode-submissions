class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Two pointers method Time: O(n) Space: O(1)
        # slow = nums[0]
        # fast = nums[0]

        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]

        #     if slow == fast:
        #         break
        
        # fast = nums[0]

        # while fast != slow:
        #     slow = nums[slow]
        #     fast = nums[fast]
        
        # return slow

        #Bit manipulation method Time: O(n*32) Space: O(1)
        n = len(nums)
        res = 0
        for b in range(32):
            x = y = 0
            mask = 1 << b
            for num in nums:
                if num & mask:
                    x += 1

            for num in range(1, n):
                if num & mask:
                    y += 1

            if x > y:
                res |= mask
        return res