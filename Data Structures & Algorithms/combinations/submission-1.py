class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #Backtracing method Time: O(k * (n!/(n - k)! * k!)) Space: O(k)
        res = []

        def backtracking(start, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return

            need = k - len(curr)
            
            for j in range(start, n - need + 2):
                curr.append(j)
                backtracking(j + 1, curr)
                curr.pop()

        backtracking(1, [])
        return res