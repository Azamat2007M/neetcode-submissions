class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Hashset method Time: O(n) Space: O(n)
        
        s_num = set(nums)
        longest = 0
            
        for num in s_num:
            if (num - 1) not in s_num:
                length = 0

                while (num + length) in s_num:
                    length += 1

                longest = max(longest, length)
        
        return longest