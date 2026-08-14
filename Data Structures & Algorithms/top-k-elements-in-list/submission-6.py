import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Method min heap Time: O(nlogk) Space: O(k)
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        res = []

        for num, freq in count.items():
            heapq.heappush(res, (freq, num))

            if len(res) > k:
                heapq.heappop(res)
        
        return [num for freq, num in res]


        #Another method with bucket sort Time: O(2n) Space: O(n)
        # count = {}
        # bucket = [[] for _ in range(len(nums) + 1)]

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # for num, freq in count.items():
        #     bucket[freq].append(num)
        
        # result = []

        # for freq in range(len(bucket) - 1, 0, -1):
        #     for num in bucket[freq]:
        #         result.append(num)

        #         if len(result) == k:
        #             return result
