import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #MinHeap method Time: O(nlogk) Space: O(k)
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

        #Quick Select method Time: O(n) or O(n^2) Space: O(1)
        # def quick_select(arr, k_id):
        #     pivot = random.choice(arr)

        #     left = [x for x in arr if x > pivot]
        #     mid = [x for x in arr if x == pivot]
        #     right = [x for x in arr if x < pivot]

        #     L, M = len(left), len(mid)

        #     if k_id < L:
        #         return quick_select(left, k_id)
        #     elif k_id < L + M:
        #         return pivot
        #     else:
        #         return quick_select(right, k_id - L - M)

        # return quick_select(nums, k - 1)