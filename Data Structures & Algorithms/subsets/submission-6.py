class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Backtracking method Time: O(n*2^n) Space: O(n)
        res = []
        subsets = []

        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i + 1)

            subsets.pop()
            dfs(i + 1)

        dfs(0)
        return res

        #Backtracking method Time: O(n*2^n) Space: O(n*2^n)
        # res = [[]]
        
        # for num in nums:
        #     res += [curr + [num] for curr in res]

        # return res