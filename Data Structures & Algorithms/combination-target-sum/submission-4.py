class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Backtracking (Optimal) method Time: O(2^(t/m)) Space: O(t/m)
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res
        
        #Backtracking method Time: O(2^(t/m)) Space: O(t/m)
        # res = []
        # def dfs(i: int, curr: list, total: int):
        #     if target == total:
        #         res.append(curr.copy())
        #         return
            
        #     if i >= len(nums) or total > target:
        #         return

        #     curr.append(nums[i])
        #     dfs(i, curr, total + nums[i])
        #     curr.pop()
        #     dfs(i + 1, curr, total)

        # dfs(0, [], 0)
        # return res