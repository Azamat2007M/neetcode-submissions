from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #Backtracing + sort method Time: O(n*n!) Space: O(n)
        # nums.sort()
        # res = []
        # visited = [False] * len(nums)

        # def backtracking(curr: list):
        #     if len(curr) == len(nums):
        #         res.append(curr.copy())
        #         return

        #     for i in range(len(nums)):
        #         if visited[i]:
        #             continue
                
        #         if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
        #             continue
                
        #         curr.append(nums[i])
        #         visited[i] = True
        #         backtracking(curr)
        #         visited[i] = False
        #         curr.pop()
            
        # backtracking([])    
        # return res

        #Backtracing + sort method Time: O(n*n!) Space: O(u)
        res = []
        counter = Counter(nums)

        def backtracking(curr: list):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    curr.append(num)

                    backtracking(curr)

                    counter[num] += 1
                    curr.pop()
        
        backtracking([])
        return res