from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        #MaxHeap method Time: O(N) Space: O(1)
        counter = Counter(s)

        max_heap = [(-ctn, char) for char, ctn in counter.items()]
        res = []
        prev = None

        while max_heap or prev:
            if not max_heap and prev:
                return ""

            ctn, char = heapq.heappop(max_heap)
            res.append(char)
            ctn += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if ctn < 0:
                prev = (ctn, char)
        
        return "".join(res)