class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #Backtracking method Time: O(2^n) Space: O(n)
        def dfs(i: int, current_bit: int) -> int:
            if i >= len(nums):
                return current_bit
            
            with_element = dfs(i + 1, current_bit ^ nums[i])
            without_element = dfs(i + 1, current_bit)

            return with_element + without_element


        return dfs(0, 0)

        #Bitwise operation Time: O(n) Space: O(1)
        # bitwise_or = 0
        # for num in nums:
        #     bitwise_or |= num
        
        # return bitwise_or << len(nums) - 1