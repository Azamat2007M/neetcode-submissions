class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Two Pointers method Time: O(n) Space: 
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            res = max(min(heights[l], heights[r]) * (r - l), res)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return res

        #Brute Force method Time: O(n^2) Space: O(1)
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         res = max(min(heights[i], heights[j]) * (j - i), res)
        
        # return res