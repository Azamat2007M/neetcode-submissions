import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr: list, low: int, high: int) -> int:
            pivot = random.randint(low, high)
            arr[pivot], arr[high] = arr[high], arr[pivot]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= arr[high]:
                    i+=1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def quick_sort(arr, low=0, high=None):
            if high is None:
                high = len(arr) - 1
            
            if low < high:
                p_idx = partition(arr, low, high)

                quick_sort(arr, low, p_idx - 1)
                quick_sort(arr, p_idx + 1, high)
            
            return arr
        
        return quick_sort(nums)

        #Quick sort Time: O(nlogn) Space: O(logn)
        #Another method with Merge sort Time: O(nlogn) Space: O(n)
        # def merge_sort(arr: list) -> list:
        #     if len(arr) <= 1:
        #         return arr
            
        #     mid = len(arr) // 2
        #     left = merge_sort(arr[:mid])
        #     right = merge_sort(arr[mid:])

        #     return merge(left, right)
        
        # def merge(left: list, right: list) -> list:
        #     res = []
        #     i = j = 0

        #     while len(left) > i and len(right) > j:
        #         if left[i] <= right[j]:
        #             res.append(left[i])
        #             i+=1
        #         else:
        #             res.append(right[j])
        #             j+=1
            
        #     res.extend(left[i:])
        #     res.extend(right[j:])

        #     return res
        
        # return merge_sort(nums)

