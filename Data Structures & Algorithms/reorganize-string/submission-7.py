from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        #Counting and Greedy method Time: O(N) Space: O(N)
        counter = Counter(s)
        n = len(s)
        most_freq_char, max_freq = counter.most_common(1)[0]

        if max_freq > (n + 1) // 2:
            return ""
        
        idx = 0
        res = [""] * n

        while counter[most_freq_char] > 0:
            res[idx] = most_freq_char
            idx += 2
            counter[most_freq_char] -= 1
        
        for char, ctn in counter.items():
            while ctn > 0:
                if idx >= n:
                    idx = 1
                
                res[idx] = char
                idx += 2
                ctn -= 1

        return "".join(res)

        #MaxHeap method Time: O(N) Space: O(1)
        # counter = Counter(s)

        # max_heap = [(-ctn, char) for char, ctn in counter.items()]
        # res = []
        # prev = None

        # while max_heap or prev:
        #     if not max_heap and prev:
        #         return ""

        #     ctn, char = heapq.heappop(max_heap)
        #     res.append(char)
        #     ctn += 1

        #     if prev:
        #         heapq.heappush(max_heap, prev)
        #         prev = None

        #     if ctn < 0:
        #         prev = (ctn, char)
        
        # return "".join(res)