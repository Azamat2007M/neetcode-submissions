from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Math+Greedy method Time: O(n) Space: O(1)
        counter = Counter(tasks)
        freq_max = max(counter.values())

        freq_max_c = sum(1 for c in counter.values() if c == freq_max)
        res = (freq_max - 1) * (n + 1) + freq_max_c

        return max(len(tasks), res)