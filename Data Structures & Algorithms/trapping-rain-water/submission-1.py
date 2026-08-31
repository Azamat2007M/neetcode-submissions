class Solution:
    def trap(self, height: List[int]) -> int:
        #Two Pointers method Time: O(n) Space: O(1)
        # l, r = 0, len(height) - 1
        # leftMax, rightMax = height[l], height[r]
        # res = 0

        # while l < r:
        #     if leftMax < rightMax:
        #         l += 1
        #         leftMax = max(leftMax, height[l])
        #         res += leftMax - height[l]
        #     else:
        #         r -= 1
        #         rightMax = max(rightMax, height[r])
        #         res += rightMax - height[r]
        
        # return res

        #Another method with extra space Time: O(n) Space: O(1)
        n = len(height)
        left_max = [0] * n
        current_max = 0
        for i in range(n):
            current_max = max(current_max, height[i])
            left_max[i] = current_max
            
        right_max = [0] * n
        current_max = 0
        for i in range(n - 1, -1, -1):
            current_max = max(current_max, height[i])
            right_max[i] = current_max
            
        total_water = 0
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            trapped_water = water_level - height[i]
            if trapped_water > 0:
                total_water += trapped_water
                
        return total_water