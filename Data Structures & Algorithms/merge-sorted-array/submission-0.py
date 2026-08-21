import heapq
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Two Pointers method Time: O(n + m) Space: O(1)
        point1 = m - 1
        point2 = n - 1

        for i in range(len(nums1) - 1, -1, -1):
            if point2 < 0:
                break
            
            if point1 >= 0 and nums1[point1] > nums2[point2]:
                nums1[i] = nums1[point1]  
                point1 -= 1
            else:
                nums1[i] = nums2[point2] 
                point2 -= 1