import random
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch Flag or 3 pointers. Time: O(n) Space: O(1)

        left, mid = 0, 0
        right = len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                mid+=1
                left+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right-=1
            
        return nums

        # Another method with Bucket Sort Time: O(2n) Space: O(1)
        # buckets = [0, 0, 0]

        # for num in nums:
        #     buckets[num] += 1

        # idx = 0

        # for color in range(3):
        #     for _ in range(buckets[color]):
        #         nums[idx] = color
        #         idx += 1
        
        # return nums

