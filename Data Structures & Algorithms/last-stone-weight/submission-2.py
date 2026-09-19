import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #MaxHeap method Time: O(nlogn) Space: O(1)
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, -(first - second))
            
        return -stones[0] if stones else 0

        #Sorting method Time: O(n^2logn) Sapce: O(n)
        # while len(stones) > 1:
        #     stones.sort()
        #     cur = stones.pop() - stones.pop()
        #     if cur:
        #         stones.append(cur)

        # return stones[0] if stones else 0