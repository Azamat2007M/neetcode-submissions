class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #MaxHeap method Time: O(n) Space: O(1)
        res = ""
        max_heap = []

        for ctn, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if ctn != 0:
                heapq.heappush(max_heap, (ctn, char))
        
        while max_heap:
            ctn, char = heapq.heappop(max_heap)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if not max_heap:
                    break

                ctn2, char2 = heapq.heappop(max_heap)
                res += char2
                ctn2 += 1

                if ctn2:
                    heapq.heappush(max_heap, (ctn2, char2))

                heapq.heappush(max_heap, (ctn, char))

            else:
                res += char
                ctn += 1

                if ctn:
                    heapq.heappush(max_heap, (ctn, char))

        return res
