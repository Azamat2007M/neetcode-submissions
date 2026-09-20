class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Backtracing + sort method Time: O(n*2^n) Space: O(n)
        # nums.sort()
        # res = []

        # def backtracking(start: int, curr: list):
        #     res.append(curr.copy())
            
        #     for j in range(start, len(nums)):
        #         if j > start and nums[j] == nums[j - 1]:
        #             continue

        #         curr.append(nums[j])
        #         backtracking(j + 1, curr)
        #         curr.pop()

        # backtracking(0, [])
        # return res

        #Alter Backtracing method Time: O(n*2^n) Space: O(n)
        nums.sort()
        res = []

        def dfs(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, curr)

        dfs(0, [])
        return res