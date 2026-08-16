class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_num = set(nums)
        longest = 0
            
        for num in nums:
            if num - 1 not in s_num:
                length = 0
                
                while num + length in s_num:
                    length += 1

                longest = max(longest, length)
        
        return longest