class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, key in enumerate(nums):
            complement = target - key
            if complement in my_dict:
                return [my_dict[complement], index]
            my_dict[key] = index
        
        return []