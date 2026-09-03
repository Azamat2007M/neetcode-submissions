class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Stack method Time: O(n) Space: O(n)
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stemp, sid = stack.pop()
                diff = i - sid
                res[sid] = diff

            stack.append([t, i])
        
        return res

        # Another method Brute Force Time: O(n^2) Space: O(1)
        # n = len(temperatures)
        # res = [0] * n

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break  

        # return res