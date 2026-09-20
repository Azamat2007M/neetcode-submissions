class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(first: int):
            if first == len(nums):
                res.append(nums.copy())
                return

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtracking(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
            
        backtracking(0)
        return res

        #Backtracing method Time: O(n) Space: O(n)
        # res = []

        # def backtracking(curr: list):
        #     if len(curr) == len(nums):
        #         res.append(curr.copy())
        #         return

        #     for num in nums:
        #         if num in curr:
        #             continue
                
        #         curr.append(num)
        #         backtracking(curr)
        #         curr.pop()
            
        # backtracking([])
        # return res