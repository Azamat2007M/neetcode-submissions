class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Another method with slicing Time: O(n) Space: O(k)
        length=len(nums)
        k%=length
        if k!=0:
            array=nums[length-k:]
            del nums[length-k:]
            nums[0:0]=array