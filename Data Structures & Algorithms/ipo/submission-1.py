import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #Sorting + MaxHeap method Time: O(nlogn) Space: O(n)
        # projects = sorted([(c, p) for c, p in zip(capital, profits)])
        # n = len(projects)
        # i = 0
        # max_heap = []

        # for _ in range(k):
        #     while i < n and projects[i][0] <= w:
        #         heapq.heappush(max_heap, -projects[i][1])
        #         i += 1

        #     if not max_heap:
        #         break
            
        #     w += -heapq.heappop(max_heap)

        # return w

        #MinHeap + MaxHeap method Time: O(nlogn) Space: O(n)
        projects = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(projects)

        max_profit = []

        for _ in range(k):
            while projects and projects[0][0] <= w:
                heapq.heappush(max_profit, -heapq.heappop(projects)[1])

            if not max_profit:
                break
            
            w += -heapq.heappop(max_profit)

        return w
