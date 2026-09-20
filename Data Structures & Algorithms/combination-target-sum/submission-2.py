class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Backtracking method Time: O(n*2^n) Space: O(n)
        res = []
        def dfs(i: int, curr: list, total: int):
            if target == total:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res

