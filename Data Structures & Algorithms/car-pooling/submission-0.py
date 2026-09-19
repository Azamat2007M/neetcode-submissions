class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #MinHeap method Time: O(nlogn) Space: O(n)
        trips.sort(key = lambda t: t[1])
        min_heap = []
        current_cap = 0

        for new_passangers, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                _, drop_passengers = heapq.heappop(min_heap)
                current_cap -= drop_passengers
            
            current_cap += new_passangers

            if current_cap > capacity:
                return False
            
            heapq.heappush(min_heap, (end, new_passangers))
    
        return True