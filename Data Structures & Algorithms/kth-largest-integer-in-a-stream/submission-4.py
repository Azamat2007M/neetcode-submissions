import heapq

class KthLargest:
    # #MinHeap method Time: O(m*logk) Space: O(k)

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums

        heapq.heapify(self.min_heap)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]

    #Sorting method Time: O(m*nlogn) Space: O(n)

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.arr = nums

    # def add(self, val: int) -> int:
    #     self.arr.append(val)
    #     self.arr.sort()

    #     return self.arr[len(self.arr) - self.k]
