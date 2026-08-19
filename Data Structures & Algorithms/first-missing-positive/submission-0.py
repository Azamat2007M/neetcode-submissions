class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        my_set = set()

        for num in nums: 
            my_set.add(num)
        for i in range(len(nums) + 1):
            if i + 1 not in my_set:
                return i + 1
            