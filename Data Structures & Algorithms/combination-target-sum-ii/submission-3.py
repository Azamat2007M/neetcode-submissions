class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #Backtracking (Optimal) method Time: O(2^(t/m)) Space: O(t/m)
        candidates.sort()
        res = []

        def backtracking(start, curr, remain):
            if remain == 0:
                res.append(curr.copy())
                return
            
            for j in range(start, len(candidates)):
                if candidates[j] > remain:
                    break

                if j > start and candidates[j] == candidates[j - 1]:
                    continue
                
                curr.append(candidates[j])
                backtracking(j + 1, curr, remain - candidates[j])
                curr.pop()

        backtracking(0, [], target)
        return res