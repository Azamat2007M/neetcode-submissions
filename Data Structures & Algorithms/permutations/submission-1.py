class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Backtracing method Time: O(n) Space: O(n)
        res = []

        def backtracking(curr: list):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in nums:
                if num in curr:
                    continue
                
                curr.append(num)
                backtracking(curr)
                curr.pop()
            
        backtracking([])
        return res