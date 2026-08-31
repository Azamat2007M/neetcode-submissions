class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Two Pointers method Time: O(n) Space: O(1)
        n = len(nums)
        k %= n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        #Another method with slicing Time: O(n) Space: O(k)
        # length=len(nums)
        # k%=length
        # if k!=0:
        #     array=nums[length-k:]
        #     del nums[length-k:]
        #     nums[0:0]=array