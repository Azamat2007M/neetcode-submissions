class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #Binary Search method Time: O(logn) Space: O(1)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + (r - l) // 2)

            if nums[mid] == target: return True

            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
            else:
                l += 1
        
        return False

        #Another Binary Search method Time: O(logn) Space: O(1)

        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r) // 2

        #     if nums[mid] == target:
        #         return True

        #     if nums[l] == nums[mid] == nums[r]:
        #         l += 1
        #         r -= 1
        #     elif nums[l] <= nums[mid]:
        #         if nums[l] <= target < nums[mid]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     else:
        #         if nums[mid] < target <= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1

        # return False