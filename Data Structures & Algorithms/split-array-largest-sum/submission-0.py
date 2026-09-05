class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        #(Missed) Another Method with DP Time: O(n^2*k) Space: O(n*k)
        n = len(nums)
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for j in range(1, k + 1):
            for i in range(1, n + 1):
                for p in range(j - 1, i):
                    current_sum = prefix_sum[i] - prefix_sum[p]
                    max_sum = max(dp[p][j - 1], current_sum)
                    dp[i][j] = min(dp[i][j], max_sum)

        return dp[n][k]