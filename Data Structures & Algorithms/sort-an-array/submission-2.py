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
