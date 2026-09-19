from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Math+Greedy method Time: O(n) Space: O(1)
        # counter = Counter(tasks)
        # freq_max = max(counter.values())

        # freq_max_c = sum(1 for c in counter.values() if c == freq_max)
        # res = (freq_max - 1) * (n + 1) + freq_max_c

        # return max(len(tasks), res)

        #MaxHeap method Time: O(n) Space: O(1)
        counter = Counter(tasks)
        max_heap = [-val for val in counter.values()]
        heapq.heapify(max_heap)
        time = 0
        cooldown = deque()

        while max_heap or cooldown:
            time += 1

            if max_heap:
                ctn = 1 + heapq.heappop(max_heap)

                if ctn != 0:
                    cooldown.append((ctn, time + n))
            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time