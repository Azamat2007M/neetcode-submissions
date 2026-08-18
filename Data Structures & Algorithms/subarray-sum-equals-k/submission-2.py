class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Prefix sum method Time: O(n) Space: O(n)
        
        prefix_counts = {0: 1}
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k

            if diff in prefix_counts:
                res += prefix_counts[diff]

            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

        return res

        # Brute-Force method Time: O(n^2) Space: O(1)
        # res = 0
        # for i in range(len(nums)):
        #     sum_a = 0
        #     for j in range(i, len(nums)):
        #         sum_a += nums[j]

        #         if sum_a == k:
        #             res+=1
        
        # return res
                