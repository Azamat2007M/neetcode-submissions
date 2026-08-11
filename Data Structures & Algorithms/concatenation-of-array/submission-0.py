class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nlen = len(nums)
        
        for i in range(nlen):
            nums.append(nums[i])
        
        return nums