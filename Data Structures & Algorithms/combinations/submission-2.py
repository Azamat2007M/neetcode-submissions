class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #Iterative method Time: O(k * (n!/(n - k)! * k!)) Space: O(k)
        res = []
        i = 0
        comb = [0] * k

        while i >= 0:
            comb[i] += 1

            if comb[i] > n:
                i -= 1
                continue
            
            if i == k - 1:
                res.append(comb.copy())
            else:
                i += 1
                comb[i] = comb[i - 1]

        return res

        #Backtracing method Time: O(k * (n!/(n - k)! * k!)) Space: O(k)
        # res = []

        # def backtracking(start, curr):
        #     if len(curr) == k:
        #         res.append(curr.copy())
        #         return

        #     need = k - len(curr)
            
        #     for j in range(start, n - need + 2):
        #         curr.append(j)
        #         backtracking(j + 1, curr)
        #         curr.pop()

        # backtracking(1, [])
        # return res